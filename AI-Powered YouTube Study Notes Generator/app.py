import re
import requests
import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import NoTranscriptFound


# PAGE CONFIG
st.set_page_config(
    page_title="YouTube Study Notes",
    page_icon="▶️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CUSTOM CSS
st.markdown("""
    <style>
    .main {
        max-width: 90%;
        margin: 0 auto;
        padding: 1rem;
    }
    .stMarkdown {
        max-width: 90%;
    }
    [data-testid="stMarkdownContainer"] {
        max-width: 90%;
    }
    .element-container {
        margin: 0.5rem 0;
    }
    </style>
""", unsafe_allow_html=True)

# UI TITLE
st.title("▶️ YouTube Study Notes Generator")
st.write(" Convert educational YouTube videos into comprehensive study notes using LLMs.")

# GROQ SETUP
GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"
MODEL_NAME = "openai/gpt-oss-20b"

PROMPT_TEMPLATE = """You are an expert educational note-taker. Convert the provided YouTube transcript into exhaustively detailed study notes.

OUTPUT STRUCTURE:

## 1: FOUNDATIONAL OVERVIEW
- Core problem or question the video addresses
- Learning objectives
- Background prerequisites
- Why this topic matters

## 2: KEY TERMS & DEFINITIONS

| Term | Definition | Context | Example |
|------|-----------|---------|---------|
| [Term] | Complete definition | How it's used | Concrete example |

Add all important terms mentioned in video in this table format.

## 3: CORE CONCEPTS & EXPLANATIONS

For each major concept:

[Concept Name]
- What it is: detailed explanation
- How it works: Step-by-step mechanism
- Why it matters: Importance
- Formula (if applicable): Write equation in plain text format (e.g., "A*v = lambda*v" or "det(A - lambda*I) = 0"), NO mathematical symbols or special notation
- Real example: Example from video in plain text

IMPORTANT: Write all formulas in plain text only. Examples:
- Instead of: (A\mathbf{v} = \lambda\mathbf{v})
- Write: A*v = lambda*v
- Instead of: \det(A-\lambda I)=0
- Write: det(A - lambda*I) = 0
- Instead of: \begin{bmatrix}3&1\\0&2\end{bmatrix}
- Write: [[3, 1], [0, 2]] or Matrix: row 1: [3, 1], row 2: [0, 2]

IMPORTANT : DO NOT MENTION THESE HEADINGS LIKE WHAT IT IS , HOW IT WORKS, WHY IT MATTERS IN THE OUTPUT. JUST WRITE THE CONTENT DIRECTLY UNDER THE CONCEPT NAME IN BULLET POINTS.

## 4: WORKED EXAMPLES

[Example Title]
- Problem: Clear problem statement
- Given: All data provided
- Solution: Show every step clearly
- Answer: Final answer with explanation

## 5: STEP-BY-STEP PROCEDURES

[Procedure Name]
- Purpose: What problem it solves
- When to use: Conditions for application
- Steps (in exact order):
  1. [Detailed step]
  2. [Detailed step]
  3. [Continue for all steps]

Formulas in plain text (e.g., "A = P*D*P^-1", NOT "A=PDP^{-1}")

## PART 6: STUDY NOTES - MUST REMEMBER

CRITICAL (Memorize exactly):
- Key facts and definitions in plain text
- Essential formulas in plain text (e.g., A*v = lambda*v)
- Important equations in plain text format

VERY IMPORTANT (Know deeply):
- Key relationships
- Important properties
- Main processes

IMPORTANT (Understand well):
- Supporting concepts
- Implementation details

Common Misconceptions:
- What students often get wrong
- Why it's wrong and the correct understanding

Special Cases & Exceptions:
- When special rules apply
- How to handle edge cases

---

CRITICAL RULES:
1. Write with FULL DETAIL - do not summarize
2. Skip NO concepts - include everything from video
3. Use precise language - explain all terminology
4. Assume reader has NO prior knowledge
5. Preserve all examples from video
6. Include all numbers, values, data
7. Explain the reasoning behind every claim
8. Use ONLY plain text for all formulas and equations - NO LaTeX, NO special symbols, NO parentheses notation
9. Make output complete and self-contained

FORMULA FORMATTING EXAMPLES (Use these exact styles):
- Eigenvalue equation: A*v = lambda*v (NOT: A\mathbf{v} = \lambda\mathbf{v})
- Matrix determinant: det(A - lambda*I) = 0 (NOT: \det(A-\lambda I)=0)
- Matrix notation: [[a, b], [c, d]] (NOT: \begin{bmatrix}a&b\\c&d\end{bmatrix})
- For vectors: v = [v1, v2, v3] (NOT: \mathbf{v} = (v_1, v_2, v_3))
- Greek letters: Use words like: lambda, mu, sigma, etc. (NOT: \lambda, \mu, \sigma)

Transcript:
[TRANSCRIPT_CONTENT]"""


def call_groq_model(prompt: str) -> str:
    """Call Groq API to generate notes."""
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    body = {
        "model": MODEL_NAME,
        "messages": [
            {
                "role": "system",
                "content": "You are a comprehensive note-generator. Generate detailed notes in clean Markdown. Use minimal but clear mathematical expressions when necessary."
            },
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.4,
        "max_tokens": 8192
    }

    resp = requests.post(GROQ_URL, headers=headers, json=body, timeout=120)

    try:
        resp.raise_for_status()
    except Exception as e:
        raise RuntimeError(f"Groq API error: {resp.text}") from e

    data = resp.json()
    return data["choices"][0]["message"]["content"]


def extract_video_id(url: str) -> str:
    """Extract YouTube video ID from URL."""
    patterns = [
        r"v=([a-zA-Z0-9_-]{11})",
        r"youtu\.be/([a-zA-Z0-9_-]{11})",
        r"embed/([a-zA-Z0-9_-]{11})",
        r"shorts/([a-zA-Z0-9_-]{11})",
    ]
    for p in patterns:
        m = re.search(p, url)
        if m:
            return m.group(1)
    if re.fullmatch(r"[a-zA-Z0-9_-]{11}", url.strip()):
        return url.strip()
    return None


def fetch_transcript_text(video_id: str) -> str:
    """Fetch transcript from YouTube."""
    ytt_api = YouTubeTranscriptApi()
    fetched = ytt_api.fetch(video_id)
    snippets = getattr(fetched, "snippets", None)

    if snippets is None:
        raw = fetched.to_raw_data()
        return " ".join(item["text"] for item in raw)

    return " ".join(snip.text for snip in snippets)


def render_notes_with_formatting(notes_text: str):
    """Render notes preserving markdown formatting while beautifying formulas."""
    import re
    
    # Split into sections by headers (##)
    sections = re.split(r'(^## .+$)', notes_text, flags=re.MULTILINE)
    
    for section in sections:
        if section.strip():
            # Check if this is a header
            if section.startswith('##'):
                st.markdown(section)
            else:
                # Process section for formulas
                lines = section.split('\n')
                buffer = []
                
                for line in lines:
                    # Check if line has a formula pattern (contains formula keywords)
                    if any(keyword in line for keyword in ['Formula:', 'formula:', 'equation:', 'Equation:']):
                        # Render buffered markdown first
                        if buffer:
                            st.markdown('\n'.join(buffer))
                            buffer = []
                        
                        # Extract and render formula
                        match = re.search(r'(.*?):\s*(.+?)(?:\s*\(NOT:|$)', line)
                        if match:
                            prefix = match.group(1) + ":"
                            formula_raw = match.group(2).strip()
                            latex_formula = convert_to_latex(formula_raw)
                            
                            st.markdown(prefix)
                            st.latex(latex_formula)
                        else:
                            buffer.append(line)
                    else:
                        # Accumulate regular markdown lines
                        buffer.append(line)
                
                # Render remaining buffered markdown
                if buffer:
                    content = '\n'.join(buffer).strip()
                    if content:
                        st.markdown(content)


def convert_to_latex(formula_text: str) -> str:
    """Convert plain text formulas to LaTeX."""
    import re
    
    result = formula_text
    
    # Replace common patterns
    replacements = [
        (r'lambda', r'\lambda'),
        (r'mu', r'\mu'),
        (r'sigma', r'\sigma'),
        (r'theta', r'\theta'),
        (r'alpha', r'\alpha'),
        (r'beta', r'\beta'),
        (r'gamma', r'\gamma'),
        (r'det\(', r'\det('),
        (r'\*', r' \cdot '),
        (r'\^', r'^'),
        (r'\[\[', r'\begin{bmatrix}'),
        (r'\]\]', r'\end{bmatrix}'),
        (r',\s*', r' & '),
        (r'\]\s*,\s*\[', r' \\ '),
    ]
    
    for pattern, replacement in replacements:
        result = re.sub(pattern, replacement, result)
    
    return result


# UI LAYOUT

st.write("")
st.write("")
col_left, col_center, col_right = st.columns([2, 1, 1])
with col_left:
    url = st.text_input(
        "Enter YouTube URL or Video ID:",
        placeholder="https://youtu.be/... or dQw4w9WgXcQ",
    )
    generate_button = st.button("Generate Notes", use_container_width=False, type="primary")

# MAIN LOGIC
if generate_button:
    if not url:
        st.error("Please enter a YouTube URL or video ID.")
        st.stop()

    video_id = extract_video_id(url)
    if not video_id:
        st.error("Invalid YouTube URL or ID.")
        st.stop()

    # Fetch transcript
    with st.spinner("Fetching transcript..."):
        try:
            transcript_text = fetch_transcript_text(video_id)
            st.success(f"Transcript fetched ({len(transcript_text)} characters)")
        except NoTranscriptFound:
            st.error("No transcript available for this video.")
            st.stop()
        except Exception as e:
            st.error(f"Error: {e}")
            st.stop()

    # Generate notes
    with st.spinner("Generating study notes..."):
        try:
            prompt_with_transcript = PROMPT_TEMPLATE.replace("[TRANSCRIPT_CONTENT]", transcript_text)
            notes = call_groq_model(prompt_with_transcript)
        except Exception as e:
            st.error(f"Error generating notes: {str(e)}")
            st.stop()

    # Display results
    st.divider()
    st.subheader("📝 Study Notes")
    render_notes_with_formatting(notes)

    # Download buttons
    st.divider()
    col1, col2 = st.columns(2)

    with col1:
        st.download_button(
            label="📥 Download as Markdown",
            data=notes,
            file_name="study_notes.md",
            mime="text/markdown",
            use_container_width=True
        )

    with col2:
        st.download_button(
            label="📄 Download as Text",
            data=notes,
            file_name="study_notes.txt",
            mime="text/plain",
            use_container_width=True
        )