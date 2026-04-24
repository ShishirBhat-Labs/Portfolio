# Insurance Cost Prediction

A machine learning project that predicts individual health insurance premium prices based on personal health profile data — with an interactive web app for real-time estimates.

---

## Links

| | |
|---|---|
| Tableau Dashboard - overview | [View](https://public.tableau.com/views/InsuranceCostPredictionOverview/Overview?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link) |
| Tableau Dashboard - Risk and demographics | [View](https://public.tableau.com/views/InsuranceCostPredictionOverview/Overview?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link) |
| Live App | [Open](https://portfolio-insurance-premium-predictor.streamlit.app/) |
| Technical Blog | [Read](https://medium.com/@shishir.r.bhat/predicting-health-insurance-premiums-with-machine-learning-an-end-to-end-data-science-project-3feaf7069108) |
| Demo Video | [Watch](#) |

---

## Overview

Insurance companies often rely on broad averages to set premiums, which can lead to inaccurate pricing for individuals. This project uses machine learning to predict annual premium costs based on an individual's age, weight, and health conditions — enabling more personalised and accurate pricing.

**Target variable:** Annual premium price (₹15,000 – ₹40,000)

---

## Dataset

986 individual records with 10 features covering demographics and health history.

| Column | Description |
|---|---|
| Age | Age of the individual (18–66 years) |
| Diabetes | Whether the individual has diabetes |
| BloodPressureProblems | Whether they have blood pressure issues |
| AnyTransplants | Whether they have had a transplant |
| AnyChronicDiseases | Presence of any chronic disease |
| Height | Height in centimetres |
| Weight | Weight in kilograms |
| KnownAllergies | Whether they have known allergies |
| HistoryOfCancerInFamily | Family history of cancer |
| NumberOfMajorSurgeries | Number of major surgeries (0–3) |

---

## What Was Done

**Exploratory Data Analysis**
- Analysed distributions of all health features and the target variable
- Found that premium price takes discrete banded values rather than being truly continuous — a key insight that shaped modelling decisions
- Identified that transplant patients almost exclusively fall in the highest premium band (₹35k–₹40k)

**Hypothesis Testing**
- Confirmed that chronic diseases, transplants, diabetes, and surgery count all lead to statistically significantly higher premiums (T-tests and ANOVA, p < 0.05)
- Found a significant association between diabetes and blood pressure problems (Chi-Square test)

**Feature Engineering**
- Derived BMI from height and weight
- Created an aggregate risk score from all binary health flags
- Added interaction terms: Age × Chronic Disease and Age × Transplant

**Modelling**
Trained and compared six models — Linear Regression, Ridge, Lasso, Decision Tree, Random Forest, and Gradient Boosting. Gradient Boosting performed best.

| Model | R² |
|---|---|
| Linear Regression | ~0.58 |
| Decision Tree | ~0.80 |
| Random Forest | ~0.88 |
| **Gradient Boosting** | **~0.92** |

> Update with your exact scores from the notebook.

Top features driving premium predictions:

| Feature | Importance |
|---|---|
| Age | 61.2% |
| Any Transplants | 8.2% |
| Weight | 7.3% |
| BMI | 6.2% |
| Number of Surgeries | 3.3% |

**Deployment**
Trained model deployed as a Streamlit web app where users can input their health details and get an instant premium estimate with a risk classification.

---

## Running Locally

```bash
git clone https://github.com/yourusername/portfolio.git
cd portfolio/insurance-cost-prediction

pip install -r requirements.txt

streamlit run app.py
```

---

## Files

```
insurance-cost-prediction/
├── app.py
├── requirements.txt
├── insurance_model.pkl
├── model.pkl
├── feature_cols.pkl
├── insurance.csv
└── Insurance_Cost_EDA_ML.ipynb
```

---

## Tech Stack

Python · Pandas · Scikit-learn · Streamlit · Tableau · Google Colab

---
