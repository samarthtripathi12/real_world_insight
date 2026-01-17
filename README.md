# Real-World Global Temperature Anomaly Analysis

Analyzes historical global temperature anomaly data using Python, with exploratory data analysis, statistical modeling, and animated visualizations.

---

## Abstract

This project analyzes global temperature anomalies from 1880–2025 using Python. It progressively explores:

1. **Raw data intake & cleaning**  
2. **Exploratory Data Analysis (EDA)**  
3. **Statistical trend analysis**  
4. **Insight isolation & visual storytelling**  

The simulations combine numerical analysis, visualization, and animation to demonstrate trends, variability, and quantitative climate insights.

---

## Why This Project

- Provides hands-on demonstration of applied data science on climate data.  
- Highlights long-term temperature trends and variability.  
- Combines EDA, statistical analysis, and visualization to extract meaningful insight.  
- Generates static plots and animated GIFs to make results intuitive.  
- Connects raw data to a defensible, singular insight for maximum impact.

---

## Development Iterations

- **v1.0:** Raw data download and storage  
- **v2.0:** Data cleaning (missing values, formatting)  
- **v3.0:** EDA plots and visualizations  
- **v4.0:** Statistical analysis and trend fitting  
- **v5.0:** Insight isolation and GIF animation  
- **v6.0:** Final summary plot combining all results  

---

## Verification

- Cleaned dataset: `data/clean/cleaned_dataset.csv`  
- Phase outputs verified visually and numerically  
- Animated GIF: `gifs/insight_evolution.gif` demonstrates full process  

---

## Requirements

- Python 3.11+  
- NumPy  
- Pandas  
- Matplotlib  
- Seaborn  
- (Optional) Plotly for interactive visuals  

---

## Phase 1: Raw Data Intake

**Scientific Question:**  
“What does the raw historical temperature data look like?”

**Description:**  
- Downloaded global land+ocean temperature anomaly CSV.  
- Preserved raw data for reproducibility.

**End-state / Outputs:**  
- `data/raw/global_temp_anomaly_annual.csv`  

**What This Proves:**  
- Ensures reproducible workflow from raw data  
- Establishes foundation for cleaning and analysis  

---

## Phase 2: Data Cleaning

**Scientific Question:**  
“Can the raw data be structured for analysis?”

**Description:**  
- Handled missing values and formatting issues  
- Normalized columns and renamed variables for clarity  
- Created a clean CSV for analysis

**End-state / Outputs:**  
- Code: `scripts/clean_data.py`  
- Clean dataset: `data/clean/cleaned_dataset.csv`  

**What This Proves:**  
- Dataset is analysis-ready  
- Cleaning process is reproducible  

---

## Phase 3: Exploratory Data Analysis (EDA)

**Scientific Question:**  
“What patterns and variability exist in the data?”

**Description:**  
- Created line plots of annual temperature anomalies  
- Generated histograms of variability  
- Calculated rolling means to highlight trends

**End-state / Outputs:**  
- Code: `scripts/eda.py`  
- Plots:  
  - `plots/eda/temp_anomaly_line.png`  
  - `plots/eda/rolling_mean_temp_anomaly.png`  
  - `plots/eda/temp_anomaly_distribution.png`  

**What This Proves:**  
- Shows variability and long-term trends  
- Provides intuition before statistical modeling  

---

## Phase 4: Statistical Analysis

**Scientific Question:**  
“What is the quantitative trend of global temperatures?”

**Description:**  
- Fit linear and polynomial trends to the cleaned data  
- Computed confidence intervals  
- Quantified trend magnitude and yearly change  

**End-state / Outputs:**  
- Code: `scripts/stat_analysis.py`  
- Plots:  
  - `plots/stat/temp_anomaly_trends.png`  
  - `plots/stat/error_bounds.png`  

**What This Proves:**  
- Trend is statistically significant  
- Variability quantified numerically  

---

## Phase 5: Insight Isolation

**Scientific Question:**  
“What single, defensible insight emerges from the analysis?”

**Description:**  
- Selected most compelling insight: **the increasing trend of global temperature anomalies**  
- Backed by statistical evidence and rolling averages  

**End-state / Outputs:**  
- `results/final_insight.txt`  

**What This Proves:**  
- Data-driven conclusion  
- Insight is clear, actionable, and verifiable  

---

## Phase 6: Visual Synthesis & GIF Animation

**Scientific Question:**  
“How can the story of temperature change be visualized dynamically?”

**Description:**  
- Combined rolling mean, trend, and yearly anomalies into a single summary plot  
- Created animated GIF showing the evolution of anomalies over time  

**End-state / Outputs:**  
- Summary plot: `plots/final/summary_plot.png`  
- Animation: `gifs/insight_evolution.gif`  

**What This Proves:**  
- Entire workflow visualized in one glance  
- Storytelling through animation strengthens impact  

---

## Phase 7: Closure

**Scientific Question:**  
“Does the workflow run end-to-end without missing outputs?”

**Description:**  
- Verified all scripts and outputs  
- Ensured reproducibility of analysis  

**End-state / Outputs:**  
- `notebooks/final_analysis.ipynb` (optional, integrates all phases)  
- Project folder fully structured and complete  

**What This Proves:**  
- Project is fully reproducible  
- All phases and outputs are verified and linked  

---

## Conclusion

This project demonstrates the application of **real-world data science** on global climate data:

1. Data intake → cleaning → EDA → statistical analysis  
2. Extracted a clear insight: global temperatures are rising steadily  
3. Visual storytelling with plots and GIF animation  

- Combines **Python programming, statistics, visualization, and reproducible workflow**  
- Ready for presentation to academic reviewers, admissions committees, or public demonstration  
- Shows applied thinking, numerical rigor, and clear insight from raw data  

---
