# Insurance Cost Prediction

A machine learning project that predicts individual health insurance premium prices based on personal health profile data — with an interactive web app for real-time estimates.

---

## Links

| | |
|---|---|
| Tableau Dashboard | [View](#) |
| Live App | [Open](#) |
| Technical Blog | [Read](#) |
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
- Key discovery: PremiumPrice takes only 24 discrete values (₹15,000 to ₹40,000) — it is banded, not continuous. This shaped every modelling decision downstream
- Transplant patients cluster almost exclusively in the ₹35k–₹40k premium band
- Age group 56–66 consistently pays the highest average premiums across all health conditions

**Hypothesis Testing**
- H1: Chronic diseases → higher premiums — T-test confirmed (p < 0.0001)
- H2: Transplants → higher premiums — T-test confirmed, strongest effect (avg ₹31,764 vs ₹23,898, p < 0.0001)
- H3: Surgery count → premium differences — One-way ANOVA confirmed (p < 0.0001)
- H4: Diabetes ↔ Blood Pressure association — Chi-Square confirmed (p < 0.0001)
- H5: Diabetes → higher premiums — T-test confirmed (p = 0.0167)

**Feature Engineering**
- `BMI` — derived from height and weight (mean 27.46, WHO categories applied)
- `RiskScore` — sum of all 6 binary health flags + surgery count (0–9 scale)
- `Age_x_Chronic` — interaction term: Age × AnyChronicDiseases
- `Age_x_Transplant` — interaction term: Age × AnyTransplants

**Outlier Handling**
- Weight (16 outliers) and BMI (22 outliers) retained — genuine high-BMI individuals, not errors
- PremiumPrice high-band values retained — legitimate pricing tiers
- BMI capped at 99th percentile (44.23) for linear model robustness
- No rows removed

**Modelling — Final Results**

| Model | MAE | RMSE | R² |
|---|---|---|---|
| Linear Regression | ₹2,603 | ₹3,484 | 0.7154 |
| Ridge Regression | ₹2,603 | ₹3,495 | 0.7135 |
| Lasso Regression | ₹2,641 | ₹3,558 | 0.7031 |
| Decision Tree | ₹1,282 | ₹2,510 | 0.8522 |
| Gradient Boosting | ₹1,381 | ₹2,384 | 0.8667 |
| **Random Forest** | **₹982** | **₹2,073** | **0.8993** |

**Best model: Random Forest Regressor**
- 5-fold cross-validation mean R²: 0.7795 (std dev: 0.0837)
- Tree-based models significantly outperformed linear models due to the discrete banded nature of PremiumPrice

**Feature Importance (Random Forest)**

| Feature | Importance |
|---|---|
| Age | 60.4% |
| Weight | 8.0% |
| AnyTransplants | 7.4% |
| BMI | 5.0% |
| Age × Chronic (interaction) | 3.8% |
| NumberOfMajorSurgeries | 3.3% |
| HistoryOfCancerInFamily | 2.0% |

**Deployment**
Trained Random Forest model deployed as a Streamlit web app with live premium prediction, BMI auto-calculation, premium band classification, risk score badge, and feature importance visualisation.

---

## Business Recommendations

1. **Transplant + surgery combinations** should go straight to specialist underwriting — the model consistently places these profiles in the ₹35k–₹40k band
2. **Age-based tiering is underutilised** — the 56–66 cohort warrants a dedicated pricing tier; grouping them with younger individuals underestimates risk
3. **Interaction features matter** — the impact of chronic diseases and transplants is compounded by age. Pricing models that ignore this will systematically underprice older high-risk clients
4. **BMI-based wellness incentives** — Weight and BMI are top predictors. Healthy BMI discounts could reduce long-term liability while attracting lower-risk customers
5. **Real-time quoting API** — the Random Forest model can be deployed as an agent-facing API for instant premium estimates during intake

---

## Running Locally

```bash
git clone https://github.com/yourusername/portfolio.git
cd portfolio/insurance-premium-predictor

pip install -r requirements.txt

streamlit run app.py
```

---

## Files

```
insurance-premium-predictor/
├── app.py
├── requirements.txt
├── insurance_model.pkl      ← Random Forest model
├── model.pkl                ← StandardScaler
├── feature_cols.pkl         ← Feature column order
├── insurance.csv
└── Insurance_Cost_EDA_ML.ipynb
```

---

## Tech Stack

Python · Pandas · Scikit-learn · Streamlit · Tableau · Google Colab

---

**[Your Name]** · [LinkedIn](#) · [GitHub](#)
