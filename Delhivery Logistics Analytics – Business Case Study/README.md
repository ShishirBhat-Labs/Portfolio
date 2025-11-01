<div align="center">

<h1><b>📦 Delhivery Logistics Analytics – Business Case Study</b></h1>
<h2><b>Data Engineering | Exploratory Analytics | Logistics Optimization</b></h2>

</div>

<p align="center">
  <img src="assets/hero.png" alt="Delhivery Logistics Analytics Banner" width="75%" />
</p>

<div align="center">
  
[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-green.svg)](https://pandas.pydata.org/)
[![NumPy](https://img.shields.io/badge/NumPy-Scientific%20Computing-red.svg)](https://numpy.org/)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-Data%20Preprocessing-orange.svg)](https://scikit-learn.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Completed-brightgreen.svg)]()

</div>

---

## 📋 Executive Summary

This project demonstrates comprehensive **data engineering and exploratory analytics** on India's largest integrated logistics platform, Delhivery. The analysis processes **144,316 delivery records** spanning **26 days** (Sep-Oct 2018), extracts actionable features from complex hierarchical trip data, and uncovers critical operational insights. The cleaned and engineered dataset enables accurate **ETA prediction models, route optimization algorithms, and demand forecasting systems**.

**Key Achievements:**
- Aggregated **144K segment-level records** to **14.7K trip-level** entities through intelligent grouping
- Engineered **15+ derived features** including temporal, geographic, and performance metrics
- Identified **3,729 delivery routes** across **29 states** and **840+ cities**
- Detected **OSRM model calibration issues:** 99.4% time underestimation, 100% distance overestimation
- Handled **73% outliers** using IQR method while preserving business-critical data
- Discovered **highest-traffic corridor:** Bangalore ↔ Mumbai with 151+ deliveries weekly

---

## 🎯 Business Problem

**Delhivery's Strategic Challenge:**

As India's fastest-growing fully integrated logistics provider, Delhivery processes millions of daily deliveries across complex multi-state networks. However, the company faced critical data challenges that hindered operational intelligence:

### **The Core Issues:**

- **Data Fragmentation:** Delivery information scattered across **multiple segment-level rows** (average 5.5 rows per trip) making holistic analysis impossible
- **Prediction Inaccuracy:** OSRM routing engine systematically underestimating delivery times, leading to broken SLAs and customer dissatisfaction
- **Route Inefficiency:** No clear visibility into corridor performance, congestion patterns, or optimization opportunities
- **Geographic Blind Spots:** Inability to identify high-demand regions and resource allocation hotspots
- **Demand Pattern Invisibility:** Missing insights into temporal trends (hourly, daily, weekly patterns)
- **Quality Assurance Gaps:** No systematic outlier detection or data quality monitoring

### **Business Opportunity:**

Implement a **data engineering pipeline** that:
- Consolidates hierarchical trip data into analysis-ready formats
- Calibrates routing predictions against actual performance
- Identifies bottleneck corridors for targeted infrastructure investment
- Reveals demand patterns for dynamic resource allocation
- Enables predictive analytics for future capacity planning

**Impact Potential:** A 5% improvement in delivery time prediction accuracy = ₹50+ crore in operational savings annually through better route planning and reduced overtime.

---

## 🔬 Methodology

### **1. Data Architecture Understanding**
- **Hierarchical Structure Recognition:** Each trip UUID comprises multiple segment rows (intermediate hub transfers)
- **Aggregation Strategy:** Segment-level → Trip-level → Route corridor analysis
- **Business Context:** FTL (consolidated) vs. Carting (flexible) delivery modes serve different operational needs

### **2. Data Processing Pipeline**
```
Raw Data (144K rows) → 
Missing Value Handling → 
DateTime Conversion → 
Trip Aggregation (26K segments) → 
Feature Engineering → 
Outlier Detection/Treatment (73% removed) → 
Categorical Encoding → 
Standardization → 
Analysis-Ready Dataset (10.8K clean records)
```

### **3. Feature Engineering Approach**

**Temporal Features:**
- Trip creation: month, day, hour, weekday, week number
- Hour bucketing: Morning (5-12), Afternoon (12-17), Evening (17-21), Night (21-5)
- Day bucketing: Start/Mid/End of month patterns
- Business day vs weekend analysis

**Geographic Features:**
- City/State/Place extraction from hierarchical location names (regex-based)
- Route corridor creation: source_name + destination_name combinations
- State-level and city-level demand patterns
- Geographic distribution analysis (29 states, 714+ source cities, 840+ destination cities)

**Performance Features:**
- Time delta calculations (od_start_time → od_end_time)
- Distance and time error metrics (OSRM vs. Actual)
- Segment aggregation: cumulative sums via cumsum()
- Trip-level metrics: sum aggregations across all segments

### **4. Analytical Techniques**

**Statistical Analysis:**
- Paired t-tests: actual_time vs OSRM_time (p < 0.001, significant difference)
- Correlation analysis: 0.892 correlation between predicted and actual time
- Hypothesis testing: OSRM model systematic bias detection
- Distribution analysis: Skewness assessment (3.5+ for distance/time metrics)

**Data Quality:**
- IQR-based outlier detection: Q1 - 1.5×IQR, Q3 + 1.5×IQR
- Outlier percentage: ~73% of records flagged (extreme distance/time cases)
- Trade-off analysis: Keep outliers to preserve business-critical long-distance/high-volume shipments

**Dimensionality Reduction:**
- One-hot encoding: route_type (FTL=0, Carting=1)
- Categorical handling: state/city variables for clustering analysis
- Standardization: StandardScaler on 9 numerical features

---

## 💻 Technical Skills & Tools Utilized

### **Data Processing & Manipulation**
- **Pandas** – Data aggregation, groupby operations, datetime handling
- **NumPy** – Numerical computations, statistical calculations
- **Regex** – Pattern extraction from unstructured location names

### **Statistical Analysis**
- **SciPy** – Paired t-tests, correlation matrices, hypothesis testing
- **Descriptive Statistics** – Mean, median, quartiles, standard deviation

### **Data Preprocessing**
- **Scikit-learn StandardScaler** – Feature standardization (mean=0, std=1)
- **IQR Method** – Outlier detection and treatment
- **Label Encoding** – Categorical variable conversion

### **Data Visualization**
- **Matplotlib & Seaborn** – Distribution plots, box plots, correlation heatmaps
- **Pair plots** – Multivariate relationship visualization
- **Bar charts & Histograms** – Categorical and continuous distributions

### **Software Engineering**
- **Git Version Control** – Code versioning and collaboration
- **Jupyter Notebooks** – Interactive EDA and documentation
- **Modular Scripts** – Separation of cleaning, feature engineering, analysis

---

## 📊 Dataset Overview

**Source:** Delhivery Operations Database (Internal)  
**Time Period:** September 12 – October 8, 2018  
**Raw Records:** 144,316 segment-level delivery entries  
**Unique Trips:** 14,787  
**Data Quality:** 99.8% complete (0.2% missing in location names)  
**Geographic Scope:** 29 states, 1,496 source centers, 1,466 destination centers

### **Data Transformation Summary**

| Stage | Records | Rows | Description |
|-------|---------|------|-------------|
| **Raw Data** | 144,316 | One row per segment | Multiple rows per trip UUID |
| **Segment Agg** | 26,222 | One row per segment | Aggregated cumulative metrics |
| **Trip Agg** | 14,787 | One row per trip | Complete trip-level features |
| **Feature Eng** | 14,787 | +15 new columns | Temporal, geographic, performance |
| **After Outlier Removal** | 10,835 | -73% records | IQR-based filtering (1.5×IQR) |
| **Final Clean** | 10,835 | Ready for ML | Encoded, standardized, analyzed |

### **Key Dataset Characteristics**

- **Delivery Modes:** FTL (65%) dominant, Carting (35%) flexible
- **Train-Test Split:** 75% training, 25% testing data
- **Geographic Concentration:** Maharashtra (18.4%), Karnataka (14.5%), Tamil Nadu (7%), Haryana (12.4%)
- **Route Diversity:** 2,165 unique source→destination routes identified
- **Temporal Span:** 26 continuous days with night-time peak (peak delivery hours)

---

## 🏆 Key Findings & Insights

### **1. OSRM Model Calibration Issues**

**Critical Discovery:** OSRM routing engine shows systematic prediction bias

| Metric | Finding | Business Impact |
|--------|---------|-----------------|
| **Time Error** | 99.4% underestimated | Promised ETAs broken regularly |
| **Distance Error** | 100% overestimated | Route planning appears inefficient |
| **Mean Time Gap** | -90.3 minutes | OSRM predicts 1.5 hours faster than actual |
| **Correlation** | 0.892 (strong) | Pattern consistent but magnitude wrong |

**Recommendation:** Recalibrate OSRM with actual Delhivery performance data; build ensemble model combining OSRM with historical performance baselines.

---

### **2. Geographic & Corridor Analysis**

**Highest-Volume States (Source):**
1. Maharashtra – 2,714 shipments (18.4%)
2. Karnataka – 2,143 shipments (14.5%)
3. Haryana – 1,823 shipments (12.4%)
4. Tamil Nadu – 1,039 shipments (7%)
5. Telangana – 784 shipments (5.3%)

**Top Source Cities:**
- Gurgaon (1,128 shipments) – Hub concentration
- Bengaluru (1,052 shipments) – Major tech/retail center
- Mumbai (968 shipments) – Business capital

**Busiest Route Corridor:**
- **Bangalore → Bengaluru (KG Airport):** 151 weekly deliveries
- **Gurgaon → Gurgaon (Bilaspur):** 123 weekly deliveries
- **Intra-Karnataka routes dominate** (Bengaluru airport hub transfers)

**Business Insight:** Delhivery's network strongly concentrated in metropolitan hubs. Tier-2 city expansion opportunity identified.

---

### **3. Temporal & Operational Patterns**

**Delivery Timing:**
- **Night Peak:** 40% of trips created between 9 PM - 5 AM (overnight dispatch)
- **Wednesday Peak:** Highest weekly delivery volume
- **Mid-Month Surge:** Days 15-20 show elevated activity
- **Entry Pattern:** Missing data Sep 4-11 (possible system outage or holiday period)

**Business Insight:** Night operations dominate; require robust 24/7 infrastructure. Weekend patterns require separate analysis.

---

### **4. Performance Metrics Summary**

| Metric | Mean | Std Dev | Min | Max | Insight |
|--------|------|---------|-----|-----|---------|
| **Actual Distance (km)** | 164 | 305 | 9 | 2,187 | High variance; multi-state routes common |
| **Actual Time (min)** | 356 | 562 | 9 | 6,265 | Wide range; 15 min to 104 hrs |
| **OSRM Distance (km)** | 160 | 271 | 6 | 2,032 | Slightly underestimated vs. actual |
| **OSRM Time (min)** | 161 | 271 | 6 | 2,032 | Severely underestimated |
| **Delivery Speed (km/hr)** | 25–30 | High variance | – | – | Traffic, load transfers impact |

---

### **5. Data Quality Assessment**

**Outlier Analysis (IQR Method):**
- **Identified Outliers:** ~7,952 records (73% of dataset)
- **Primary Causes:** Long-distance inter-state trips, high-volume consolidation shipments
- **Decision:** Remove extreme outliers to ensure model validity, but business context suggests keeping most for realism

**Missing Values:**
- Source/Destination names: 0.2% (negligible)
- All performance metrics: 0% complete
- **Assessment:** Excellent data quality for operational analytics

---

## 💡 Business Recommendations

### **Immediate Actions**

#### **1. OSRM Recalibration Project**
- Conduct comprehensive audit: compare OSRM predictions vs. actual performance on all routes
- Identify systematic biases by route type (FTL vs. Carting), distance band, and geography
- Build correction factors: Multiply OSRM time by 2.5x, OSRM distance by 1.1x (preliminary)
- Implement A/B testing: Use corrected ETAs vs. raw OSRM for customer promises

#### **2. Data Quality Baseline**
- Establish daily monitoring: Track missing values, outliers, data freshness
- Alert thresholds: Flag if >5% records missing, outlier rate >80%
- Root cause analysis: Investigate Sep 4-11 data gaps

#### **3. Corridor Performance Dashboard**
- Create real-time visibility: Top 50 routes, average delivery time, SLA breach rate
- Benchmark leaders: Identify high-efficiency corridors (e.g., Gurgaon→Gurgaon)
- Lag detection: Flag routes with OSRM vs. actual deltas >2 hours

### **Short-Term Initiatives**

#### **1. Route Optimization**
- **FTL Consolidation:** Increase FTL adoption from current 65% to 75% on high-volume routes
- **Hub Strategy:** Leverage Bengaluru/Gurgaon/Mumbai hub concentration for transshipment efficiency
- **Carting Optimization:** Use carting for last-mile (avoiding long-distance inefficiency)
- **Expected Benefit:** 10-15% time reduction on major corridors

#### **2. Geographic Expansion Targeting**
- **Underserved States:** Focus growth in AP, Kerala, West Bengal (currently <5% share)
- **Tier-2 City Strategy:** Build hubs in secondary metros (Pune, Hyderabad, Ahmedabad)
- **Infrastructure Investment:** Align capex with demand concentration (Maharashtra 18%, Karnataka 14%)

#### **3. Temporal Capacity Planning**
- **Night Shift Staffing:** Scale resources for 40% night-time dispatch volume
- **Peak Preparation:** Stage extra capacity days 15-20 (mid-month surge)
- **Cost Optimization:** Lower rates/incentives during off-peak hours

### **Medium-Term Strategic Initiatives**

#### **1. Predictive Analytics Foundation**
- Build **ETA Prediction Model:** Using actual historical data + weather + traffic API
- Train **Demand Forecasting Model:** Predict daily volumes by route, enable dynamic pricing
- Implement **Anomaly Detection:** Flag unusual delivery patterns for investigation

#### **2. Real-Time Network Optimization**
- Develop **Dynamic Routing Engine:** Replace static OSRM with ML-powered routing
- **Live Rerouting:** Real-time optimization based on traffic, vehicle location, order priority
- **Load Balancing:** Auto-distribute orders to optimal routes, hubs

#### **3. Customer Experience Enhancement**
- **Accurate ETAs:** Publish realistic delivery windows (address 99.4% OSRM underestimation)
- **Proactive Communication:** Alert customers before potential delays
- **SLA Alignment:** Reset commitments based on actual performance, rebuild trust

### **Long-Term Strategic Initiatives**

1. **Network Design Optimization:** Evaluate hub locations, rebalance capacity allocation
2. **Technology Integration:** Real-time IoT tracking, vehicle telematics, ML-powered dispatch
3. **Sustainability:** Optimize routes for carbon footprint reduction
4. **Competitive Positioning:** Use superior analytics for faster, cheaper, more reliable delivery
5. **Revenue Expansion:** Tiered pricing based on route complexity, time urgency, geography

---

## 📈 Advanced Analytics Opportunities

### **1. Predictive Modeling**
- **Time-to-Delivery Prediction:** Random Forest/XGBoost on engineered features (R² > 0.85 target)
- **Outlier Time Detection:** Identify problematic routes for intervention
- **Delivery Success Probability:** Predict SLA compliance by route and shipment characteristics

### **2. Clustering & Segmentation**
- **Route Clustering:** Group similar routes by distance, time, traffic patterns
- **Customer Segmentation:** Premium (fast) vs. economy (cost-optimized) delivery pathways
- **Hub Efficiency Clustering:** Identify best-performing transfer hubs for benchmarking

### **3. Time Series Forecasting**
- **Daily Volume Forecasting:** ARIMA/Prophet for capacity planning
- **Seasonal Decomposition:** Identify monthly/weekly/daily patterns
- **Anomaly Detection:** Flag unusual volume spikes or drops

### **4. Network Flow Optimization**
- **Supply-Demand Matching:** Balance shipment sources with destination capacity
- **Hub Allocation:** Optimal routing through multi-hop network
- **Vehicle Utilization:** Maximize load factors on FTL shipments

---

## 📁 Repository Structure

```
delhivery-logistics-analytics/
├── assets/
├── notebooks/
│   └── Delhivery_Analytics_Complete.ipynb    # Full analysis notebook
├── requirements.txt                    # Python dependencies
├── Sample_Data.png                    # Python dependencies
├── .gitignore                          # Git ignore patterns
├── LICENSE                             # MIT License
└── README.md                           # This file
```

---

## 📚 Key Findings Summary

### **Data Transformation Efficiency**
- Successfully consolidated 144,316 segment records → 14,787 logical trips
- Engineered 15+ features from raw timestamps and location names
- Achieved 99.8% data quality (only 0.2% missing values)

### **OSRM Model Findings**
| Aspect | Finding | Action |
|--------|---------|--------|
| Time Prediction | 99.4% underestimated (mean -90 min) | Implement 2.5x correction factor |
| Distance Prediction | 100% overestimated (mean +18 km) | Apply 1.1x correction; investigate |
| Model Correlation | 0.892 (strong pattern) | Systematic bias, not random error |

### **Geographic Intelligence**
- **Top States:** Maharashtra (18%), Karnataka (15%), Haryana (12%)
- **Hub Concentration:** Gurgaon, Bengaluru, Mumbai dominate
- **Growth Opportunity:** Underserved tier-2 cities (Pune, Hyderabad, Ahmedabad)

### **Operational Insights**
- Night-time dominance (40% deliveries 9 PM - 5 AM)
- Wednesday peak, mid-month surge pattern
- High variance in delivery times (9 min to 6,265 min = 104 hours)

---

## ⚠️ Data Processing Considerations

### **Hierarchical Data Aggregation**
- Each trip_uuid may contain 3-10 segment rows (intermediate transfers)
- Aggregation rules matter:
  - **Numeric (distance/time):** Use `sum()` for cumulative metrics
  - **Categorical (source/destination):** Use `first()` for source, `last()` for destination
  - **Temporal:** Use `first()` for start, `last()` for end

### **Outlier Treatment Trade-offs**
- IQR method removed 7,952 records (73%)
- Decision: Keep long-distance outliers (valid business cases) but remove extreme cases
- Alternative: Use robust scaling (Huber scaler) instead of removal for ML models

### **Geographic Feature Extraction**
- Location names follow pattern: `City_Place_Code (State)`
- Regex pattern: `^(?P<city>[^\s_]+)_?(?P<place>[^\(\)]*)\s?\((?P<state>[A-Za-z\s&]+)\)$`
- Note: "Bangalore" vs "Bengaluru" standardization required

---

<div align="center">

### ⭐ **If this project demonstrates valuable skills in data engineering, logistics analytics, or business intelligence, please give it a star!** ⭐

</div>
