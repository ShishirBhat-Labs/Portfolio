import streamlit as st
import pickle
import numpy as np
import pandas as pd

# ── Page config ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Insurance Premium Calculator",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ── Custom CSS ─────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=DM+Sans:wght@300;400;500;600&display=swap');

/* Base */
html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

.stApp {
    background: #f0f4f8;
}

/* Header */
.hero {
    background: linear-gradient(135deg, #1a1f3c 0%, #2d3561 60%, #1e4d8c 100%);
    border-radius: 20px;
    padding: 48px 40px 40px 40px;
    margin-bottom: 32px;
    position: relative;
    overflow: hidden;
}
.hero::before {
    content: '';
    position: absolute;
    top: -60px; right: -60px;
    width: 220px; height: 220px;
    background: rgba(255,255,255,0.04);
    border-radius: 50%;
}
.hero::after {
    content: '';
    position: absolute;
    bottom: -40px; left: 30%;
    width: 140px; height: 140px;
    background: rgba(255,255,255,0.03);
    border-radius: 50%;
}
.hero-title {
    font-family: 'DM Serif Display', serif;
    font-size: 2.4rem;
    color: #ffffff;
    margin: 0 0 8px 0;
    line-height: 1.2;
}
.hero-sub {
    color: #a8b8d8;
    font-size: 1rem;
    font-weight: 300;
    margin: 0;
}
.hero-badge {
    display: inline-block;
    background: rgba(255,255,255,0.12);
    color: #c8d8f0;
    font-size: 0.72rem;
    font-weight: 600;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    padding: 4px 12px;
    border-radius: 20px;
    margin-bottom: 16px;
    border: 1px solid rgba(255,255,255,0.15);
}

/* Section cards */
.section-card {
    background: #ffffff;
    border-radius: 16px;
    padding: 28px 28px 24px 28px;
    margin-bottom: 20px;
    box-shadow: 0 2px 12px rgba(0,0,0,0.06);
    border: 1px solid #e8ecf0;
}
.section-label {
    font-size: 0.7rem;
    font-weight: 600;
    letter-spacing: 1.8px;
    text-transform: uppercase;
    color: #1e4d8c;
    margin-bottom: 18px;
    display: flex;
    align-items: center;
    gap: 8px;
}
.section-label::after {
    content: '';
    flex: 1;
    height: 1px;
    background: #e8ecf0;
}

/* Result card */
.result-card {
    background: linear-gradient(135deg, #1a1f3c 0%, #1e4d8c 100%);
    border-radius: 20px;
    padding: 40px 32px;
    text-align: center;
    box-shadow: 0 8px 32px rgba(30,77,140,0.25);
    margin-top: 8px;
}
.result-label {
    color: #a8b8d8;
    font-size: 0.78rem;
    font-weight: 600;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 12px;
}
.result-amount {
    font-family: 'DM Serif Display', serif;
    font-size: 3.2rem;
    color: #ffffff;
    line-height: 1;
    margin-bottom: 8px;
}
.result-range {
    color: #a8b8d8;
    font-size: 0.85rem;
    margin-bottom: 24px;
}
.result-band {
    display: inline-block;
    background: rgba(255,255,255,0.12);
    color: #ffffff;
    border: 1px solid rgba(255,255,255,0.2);
    border-radius: 20px;
    padding: 6px 18px;
    font-size: 0.82rem;
    font-weight: 500;
}

/* Risk badge */
.risk-pill {
    display: inline-block;
    border-radius: 20px;
    padding: 5px 16px;
    font-size: 0.78rem;
    font-weight: 600;
    margin-top: 14px;
}
.risk-low    { background: #e6f4ea; color: #1e7e34; }
.risk-medium { background: #fff3cd; color: #856404; }
.risk-high   { background: #fde8e8; color: #c0392b; }

/* Feature importance bar */
.fi-row {
    display: flex;
    align-items: center;
    margin-bottom: 10px;
    gap: 10px;
}
.fi-label {
    font-size: 0.8rem;
    color: #4a5568;
    width: 170px;
    flex-shrink: 0;
    font-weight: 500;
}
.fi-bar-bg {
    flex: 1;
    height: 8px;
    background: #edf2f7;
    border-radius: 4px;
    overflow: hidden;
}
.fi-bar-fill {
    height: 100%;
    border-radius: 4px;
    background: linear-gradient(90deg, #1e4d8c, #4a90d9);
}
.fi-pct {
    font-size: 0.75rem;
    color: #718096;
    width: 38px;
    text-align: right;
    flex-shrink: 0;
}

/* Streamlit overrides */
div[data-testid="stSlider"] > div { padding-top: 4px; }
.stSelectbox label, .stSlider label, .stRadio label { 
    font-size: 0.85rem !important; 
    font-weight: 500 !important;
    color: #2d3748 !important;
}
div[data-testid="stButton"] button {
    background: linear-gradient(135deg, #1a1f3c, #1e4d8c) !important;
    color: white !important;
    border: none !important;
    border-radius: 12px !important;
    padding: 14px 0 !important;
    font-size: 1rem !important;
    font-weight: 600 !important;
    width: 100% !important;
    letter-spacing: 0.5px;
    box-shadow: 0 4px 16px rgba(30,77,140,0.3) !important;
    transition: all 0.2s ease !important;
}
div[data-testid="stButton"] button:hover {
    box-shadow: 0 6px 24px rgba(30,77,140,0.45) !important;
    transform: translateY(-1px) !important;
}
</style>
""", unsafe_allow_html=True)


# ── Load models ────────────────────────────────────────────────────────────────
@st.cache_resource
def load_artifacts():
    with open('insurance_model.pkl', 'rb') as f:
        model = pickle.load(f)
    with open('model.pkl', 'rb') as f:          # scaler saved as model.pkl
        scaler = pickle.load(f)
    with open('feature_cols.pkl', 'rb') as f:
        feature_cols = pickle.load(f)
    return model, scaler, feature_cols

model, scaler, feature_cols = load_artifacts()

# Feature importances from your GBM output
FEATURE_IMPORTANCE = {
    'Age': 0.6115,
    'AnyTransplants': 0.0821,
    'Weight': 0.0727,
    'BMI': 0.0621,
    'Age_x_Chronic': 0.0370,
    'NumberOfMajorSurgeries': 0.0330,
    'Age_x_Transplant': 0.0210,
    'Height': 0.0204,
    'AnyChronicDiseases': 0.0132,
    'RiskScore': 0.0118,
    'BloodPressureProblems': 0.0069,
    'KnownAllergies': 0.0033,
    'Diabetes': 0.0021,
    'HistoryOfCancerInFamily': 0.0020,
}


# ── Helper functions ───────────────────────────────────────────────────────────
def compute_features(age, height, weight, diabetes, bp, transplants,
                     chronic, allergies, cancer_hist, surgeries):
    bmi = weight / ((height / 100) ** 2)
    risk_score = (diabetes + bp + transplants + chronic +
                  allergies + cancer_hist + surgeries)
    age_x_chronic   = age * chronic
    age_x_transplant = age * transplants
    return {
        'Age': age, 'Diabetes': diabetes, 'BloodPressureProblems': bp,
        'AnyTransplants': transplants, 'AnyChronicDiseases': chronic,
        'Height': height, 'Weight': weight, 'KnownAllergies': allergies,
        'HistoryOfCancerInFamily': cancer_hist,
        'NumberOfMajorSurgeries': surgeries,
        'BMI': round(bmi, 2), 'RiskScore': risk_score,
        'Age_x_Chronic': age_x_chronic, 'Age_x_Transplant': age_x_transplant
    }

def get_risk_label(risk_score):
    if risk_score <= 1:
        return "Low Risk", "risk-low"
    elif risk_score <= 3:
        return "Moderate Risk", "risk-medium"
    else:
        return "High Risk", "risk-high"

def get_premium_band(premium):
    if premium < 20000:
        return "🟢 Standard Band  (₹15k – ₹20k)"
    elif premium < 28000:
        return "🟡 Elevated Band  (₹20k – ₹28k)"
    elif premium < 35000:
        return "🟠 High Band  (₹28k – ₹35k)"
    else:
        return "🔴 Premium Band  (₹35k – ₹40k)"


# ── UI ─────────────────────────────────────────────────────────────────────────

# Hero
st.markdown("""
<div class="hero">
    <div class="hero-badge">🏥 ML-Powered · Gradient Boosting</div>
    <div class="hero-title">Insurance Premium Calculator</div>
    <p class="hero-sub">Enter individual health profile details to estimate annual insurance premium cost</p>
</div>
""", unsafe_allow_html=True)

# ── Layout: inputs left, result right ─────────────────────────────────────────
left, right = st.columns([1.6, 1], gap="large")

with left:

    # ── Section 1: Demographics ──────────────────────────────────────────────
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-label">👤 Demographics</div>', unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    with c1:
        age = st.slider("Age (years)", min_value=18, max_value=66, value=35, step=1)
    with c2:
        height = st.slider("Height (cm)", min_value=145, max_value=188, value=165, step=1)
    with c3:
        weight = st.slider("Weight (kg)", min_value=51, max_value=132, value=70, step=1)

    # Live BMI display
    bmi_val = weight / ((height / 100) ** 2)
    if bmi_val < 18.5:
        bmi_cat, bmi_col = "Underweight", "#3498db"
    elif bmi_val < 25:
        bmi_cat, bmi_col = "Normal", "#27ae60"
    elif bmi_val < 30:
        bmi_cat, bmi_col = "Overweight", "#f39c12"
    else:
        bmi_cat, bmi_col = "Obese", "#e74c3c"

    st.markdown(
        f'<p style="font-size:0.82rem; color:#718096; margin-top:4px;">'
        f'Calculated BMI: <strong style="color:{bmi_col}">{bmi_val:.1f} — {bmi_cat}</strong></p>',
        unsafe_allow_html=True
    )
    st.markdown('</div>', unsafe_allow_html=True)

    # ── Section 2: Health Conditions ────────────────────────────────────────
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-label">🩺 Health Conditions</div>', unsafe_allow_html=True)

    c4, c5 = st.columns(2)
    with c4:
        diabetes   = st.radio("Diabetes",               ["No", "Yes"], horizontal=True)
        bp         = st.radio("Blood Pressure Problems", ["No", "Yes"], horizontal=True)
        transplants = st.radio("Any Transplants",        ["No", "Yes"], horizontal=True)
    with c5:
        chronic    = st.radio("Any Chronic Diseases",    ["No", "Yes"], horizontal=True)
        allergies  = st.radio("Known Allergies",         ["No", "Yes"], horizontal=True)
        cancer_hist = st.radio("Family History of Cancer", ["No", "Yes"], horizontal=True)

    st.markdown('</div>', unsafe_allow_html=True)

    # ── Section 3: Surgical History ─────────────────────────────────────────
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-label">🔬 Surgical History</div>', unsafe_allow_html=True)

    surgeries = st.select_slider(
        "Number of Major Surgeries",
        options=[0, 1, 2, 3],
        value=0,
        format_func=lambda x: f"{x} {'surgery' if x == 1 else 'surgeries'}"
    )
    st.markdown('</div>', unsafe_allow_html=True)

    # ── Predict button ───────────────────────────────────────────────────────
    predict_btn = st.button("Calculate Premium Estimate →")


# ── Right column: result ───────────────────────────────────────────────────────
with right:

    # Convert radio to binary
    d  = 1 if diabetes    == "Yes" else 0
    b  = 1 if bp          == "Yes" else 0
    t  = 1 if transplants == "Yes" else 0
    ch = 1 if chronic     == "Yes" else 0
    al = 1 if allergies   == "Yes" else 0
    ca = 1 if cancer_hist == "Yes" else 0

    feats = compute_features(age, height, weight, d, b, t, ch, al, ca, surgeries)
    input_df = pd.DataFrame([feats])[feature_cols]
    input_scaled = scaler.transform(input_df)
    predicted = model.predict(input_df)[0]          # GBM doesn't need scaled input
    predicted = max(15000, min(40000, round(predicted, -2)))   # clamp to valid range

    risk_label, risk_class = get_risk_label(feats['RiskScore'])
    band = get_premium_band(predicted)

    if predict_btn or True:   # show result always, updates live with sliders
        st.markdown(f"""
        <div class="result-card">
            <div class="result-label">Estimated Annual Premium</div>
            <div class="result-amount">₹{predicted:,.0f}</div>
            <div class="result-range">Prediction range: ₹{max(15000, predicted-2000):,.0f} – ₹{min(40000, predicted+2000):,.0f}</div>
            <div class="result-band">{band}</div>
            <br/>
            <span class="risk-pill {risk_class}">{risk_label}</span>
        </div>
        """, unsafe_allow_html=True)

    # ── Profile summary ──────────────────────────────────────────────────────
    st.markdown('<div class="section-card" style="margin-top:20px;">', unsafe_allow_html=True)
    st.markdown('<div class="section-label">📋 Profile Summary</div>', unsafe_allow_html=True)

    summary_data = {
        "Age": f"{age} yrs",
        "BMI": f"{bmi_val:.1f} ({bmi_cat})",
        "Risk Score": f"{feats['RiskScore']} / 9",
        "Surgeries": surgeries,
        "Active Conditions": sum([d, b, t, ch, al, ca])
    }
    for k, v in summary_data.items():
        st.markdown(
            f'<div style="display:flex; justify-content:space-between; '
            f'padding:6px 0; border-bottom:1px solid #f0f4f8; font-size:0.85rem;">'
            f'<span style="color:#718096;">{k}</span>'
            f'<span style="font-weight:600; color:#2d3748;">{v}</span></div>',
            unsafe_allow_html=True
        )
    st.markdown('</div>', unsafe_allow_html=True)

    # ── Feature importance bars ──────────────────────────────────────────────
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-label">📊 Key Premium Drivers</div>', unsafe_allow_html=True)

    top_features = sorted(FEATURE_IMPORTANCE.items(), key=lambda x: x[1], reverse=True)[:7]
    max_imp = top_features[0][1]

    bars_html = ""
    for feat, imp in top_features:
        pct = imp / max_imp * 100
        label = feat.replace('_x_', ' × ').replace('_', ' ')
        bars_html += f"""
        <div class="fi-row">
            <div class="fi-label">{label}</div>
            <div class="fi-bar-bg">
                <div class="fi-bar-fill" style="width:{pct:.1f}%"></div>
            </div>
            <div class="fi-pct">{imp:.1%}</div>
        </div>"""

    st.markdown(bars_html, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)


# ── Footer ─────────────────────────────────────────────────────────────────────
st.markdown("""
<div style="text-align:center; padding:32px 0 16px; color:#a0aec0; font-size:0.78rem;">
    Powered by Gradient Boosting · Trained on 986 insurance records · For educational purposes only
</div>
""", unsafe_allow_html=True)
