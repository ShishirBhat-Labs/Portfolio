<div align="center">

# 🎓 Jamboree Business Case Study - Graduate Admission Prediction
# 📈 Machine learning - Linear Regression

</div>

<p align="center">
  
  <img src="assets/hero.png" alt="Project banner" width="75%" />
</p>

## 📌 Context

**Jamboree** has helped thousands of students secure admissions to top universities abroad.  
Whether it's **GMAT, GRE, or SAT**, their unique teaching and problem-solving methods have enabled students to achieve **maximum scores with minimum effort**.

Recently, Jamboree launched a **Graduate Admission Probability Feature** 🎯 on their website, where students can enter their profile details and instantly check their **chances of getting into Ivy League or top global universities**.

👉 **Our role?** Build the data-driven backbone for this feature using machine learning and statistical analysis.

---

Report link - [IPYNB](https://github.com/ShishirBhat-Labs/Portfolio/blob/main/Jamboree%20Admissions%20Prediction%20Business%20Case%20study/Notebook/Jamboree%20admission%20prediction%20case%20study.ipynb) , [PDF](https://github.com/ShishirBhat-Labs/Portfolio/blob/main/Jamboree%20Admissions%20Prediction%20Business%20Case%20study/Report/Jamboree%20admission%20prediction%20case%20study.pdf)

---

## 🎯 Project Objectives

- **Predict graduate school admission chances** with high accuracy using machine learning
- **Identify key factors** that drive admission decisions  
- **Understand relationships** between academic metrics and admission probability
- **Provide actionable insights** for students and counselors  
- **Create a deployable model** for Jamboree's website feature

---

## 📊 Dataset Overview

**Source:** Jamboree Education  
**Size:** 500 records × 8 features (after preprocessing)

| Feature | Description | Range | Type |
|---------|-------------|-------|------|
| **GRE Score** | Graduate Record Examination | 290-340 | Continuous |
| **TOEFL Score** | English proficiency test | 92-120 | Continuous |
| **University Rating** | Institution prestige rating | 1-5 | Ordinal |
| **SOP** | Statement of Purpose strength | 1-5 | Continuous |
| **LOR** | Letter of Recommendation strength | 1-5 | Continuous |
| **CGPA** | Cumulative Grade Point Average | 6.8-9.9 | Continuous |
| **Research** | Research experience | 0/1 | Binary |
| **Admission Chance** | Probability of admission | 0.34-0.97 | **Target Variable** |

---

## 🔬 Machine Learning Approach

### **Algorithm Selection**
- **Linear Regression** (Baseline model)
- **Lasso Regression** (L1 regularization for feature selection)
- **Ridge Regression** (L2 regularization for multicollinearity)

### **Model Performance**
- **Best Model:** Lasso Regression (α=0.001)
- **Test R² Score:** 82.0% variance explained
- **RMSE:** 0.061 (6.1% average error)
- **Cross-validation:** Consistent performance across all splits

### **Statistical Validation**
- **OLS Regression** with statsmodels for coefficient significance testing
- **VIF Analysis** confirmed no multicollinearity issues (all VIF < 5)
- **Assumption Testing** for linearity, normality, and homoscedasticity

---

## 📈 Key Findings

### **Top Admission Predictors** (Ranked by Impact)
1. **CGPA (0.882 correlation)** - Strongest predictor, each grade point increases admission chance by 6.8%
2. **GRE Score (0.810 correlation)** - Critical standardized test metric
3. **TOEFL Score (0.792 correlation)** - Essential for international students
4. **Research Experience** - Binary boost of +15.5 percentage points
5. **LOR & SOP** - Moderate impact on final decision

### **Business Insights**
- **Research experience** provides the highest single intervention impact
- **University rating** has surprisingly low independent effect
- **Academic metrics** (CGPA, GRE, TOEFL) form the core evaluation trinity
- Model achieves **production-ready accuracy** for deployment

---

## 🛠 Technical Implementation

### **Data Processing Pipeline**
```python
# Data cleaning & preprocessing
- Handled missing values (0% missing data)
- Outlier detection using IQR method
- Feature scaling with StandardScaler
- Train-test split (80-20) with stratification
```

### **Machine Learning Models**
```python
# Model comparison framework
- Linear Regression (baseline)
- Lasso Regression (feature selection, α=0.001)
- Ridge Regression (regularization, α=0.0001)
- Cross-validation for hyperparameter tuning
```

### **Statistical Analysis**
```python
# Comprehensive validation
- OLS regression with statsmodels
- Variance Inflation Factor (VIF) analysis
- Residual diagnostics & assumption testing
- Confidence intervals & significance testing
```

---

## 🚀 Getting Started

### **Prerequisites**
```bash
Python 3.7+
pip install -r requirements.txt
```

### **Quick Start**
```bash
# Clone repository
git clone https://github.com/yourusername/jamboree-admission-prediction
cd jamboree-admission-prediction

# Install dependencies
pip install -r requirements.txt

# Run analysis
jupyter notebook notebooks/Jamboree_Analysis.ipynb
```

---

## 📊 Results Summary

| Metric | Linear Regression | Lasso | Ridge | **Best Model** |
|--------|------------------|--------|--------|----------------|
| **Test R²** | 0.8188 | **0.8192** | 0.8188 | **Lasso** |
| **Test RMSE** | 0.0609 | **0.0608** | 0.0609 | **Lasso** |
| **Train R²** | 0.8211 | 0.8210 | 0.8211 | Lasso |
| **Overfitting** | Minimal | Minimal | Minimal | ✅ |

**Key Insights:**
- 82% of admission variance explained by the model
- CGPA is the dominant predictor (68% higher impact than GRE)
- Research experience provides 15.5% probability boost
- Model ready for production deployment

---

## 💡 Business Impact

### **For Students:**
- **Personalized guidance** on which areas to focus improvement efforts
- **What-if scenario planning** to optimize admission strategy
- **Realistic expectations** based on current profile strength

### **For Jamboree:**
- **Competitive differentiation** with data-driven admission counseling
- **Resource optimization** by focusing on high-impact factors
- **Revenue growth** through premium data-backed consulting services

---

## 🛠 Tech Stack

**Data Analysis & Preprocessing:**
- `pandas`, `numpy` - Data manipulation
- `matplotlib`, `seaborn` - Advanced visualizations
- `scipy` - Statistical testing

**Machine Learning:**
- `scikit-learn` - ML algorithms & evaluation
- `statsmodels` - Statistical regression analysis
- `joblib` - Model serialization

**Development Tools:**
- `jupyter` - Interactive analysis environment
- `git` - Version control
- `pytest` - Testing framework (future enhancement)

---

## 📈 Future Enhancements

- **Deep Learning Models** (Neural Networks) for non-linear patterns
- **Feature Engineering** (polynomial features, interaction terms)
- **Real-time API** deployment using Flask/FastAPI
- **A/B Testing Framework** for continuous model improvement
- **Advanced Ensemble Methods** (XGBoost, LightGBM)

---

## 📈 Repo structure


├── assets/
├── Notebook and Report/
│   ├── Jamboree admission prediction case study.ipynb          # Jupyter notebooks
│   └── Jamboree admission prediction case study.pdf            # Project reports
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt

⭐ **If this project helped you understand graduate admission analytics, please star the repository!** ⭐

---

*Built with ❤️ for data-driven education decisions*
