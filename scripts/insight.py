# scripts/insight.py

import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np

# -----------------------------
# 1️⃣ Folder paths
# -----------------------------
clean_folder = 'data/clean/'
output_folder = 'outputs/'
os.makedirs(output_folder, exist_ok=True)

clean_file = os.path.join(clean_folder, 'cleaned_temp_anomaly.csv')
df = pd.read_csv(clean_file)

# -----------------------------
# 2️⃣ Calculate trends
# -----------------------------
# Compute linear trend for entire dataset
years = df['Year']
temps = df['Temp_Anomaly']
coeffs = np.polyfit(years, temps, 1)
slope = coeffs[0]
intercept = coeffs[1]

print(f"Linear trend: slope = {slope:.4f} °C/year")

# Split into two periods: 1880-1950 vs 1951-2025
df_early = df[df['Year'] <= 1950]
df_late = df[df['Year'] > 1950]

slope_early, _ = np.polyfit(df_early['Year'], df_early['Temp_Anomaly'], 1)
slope_late, _ = np.polyfit(df_late['Year'], df_late['Temp_Anomaly'], 1)

print(f"Slope 1880-1950: {slope_early:.4f} °C/year")
print(f"Slope 1951-2025: {slope_late:.4f} °C/year")

# -----------------------------
# 3️⃣ Visualize the trends
# -----------------------------
plt.figure(figsize=(10,5))
plt.plot(df['Year'], df['Temp_Anomaly'], color='red', label='Temp Anomaly', alpha=0.5)

# Linear trend lines
plt.plot(years, slope*years + intercept, color='black', linestyle='--', label='Overall Trend')
plt.plot(df_early['Year'], slope_early*df_early['Year'] + intercept, color='blue', linestyle='--', label='1880-1950 Trend')
plt.plot(df_late['Year'], slope_late*df_late['Year'] + intercept, color='orange', linestyle='--', label='1951-2025 Trend')

plt.xlabel('Year')
plt.ylabel('Temperature Anomaly (°C)')
plt.title('Global Temperature Trends')
plt.legend()
plt.grid(True)
plt.tight_layout()

trend_file = os.path.join(output_folder, 'temperature_trends.png')
plt.savefig(trend_file)
plt.close()
print(f"✅ Trend plot saved: {trend_file}")

# -----------------------------
# 4️⃣ Insight Summary
# -----------------------------
insight_summary = f"""
📊 Phase 4 Insight:

1️⃣ Overall, global temperatures have increased at a rate of {slope:.4f} °C/year since 1880.

2️⃣ The rate was slower in the early period (1880-1950): {slope_early:.4f} °C/year

3️⃣ The warming accelerated significantly in the late period (1951-2025): {slope_late:.4f} °C/year

🔹 Insight: Human activity and industrialization in the second half of the 20th century are correlated with a **marked acceleration in global warming**. This quantitative analysis provides a clear story from raw temperature data.
"""

print(insight_summary)

# Optional: save insight to text file
insight_file = os.path.join(output_folder, 'insight.txt')
with open(insight_file, 'w') as f:
    f.write(insight_summary)

print(f"✅ Insight summary saved: {insight_file}")
