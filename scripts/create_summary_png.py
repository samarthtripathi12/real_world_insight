import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

# Load cleaned data
df = pd.read_csv('data/clean/cleaned_temp_anomaly.csv')

# Compute rolling mean and trend
df['Rolling_Mean'] = df['Temp_Anomaly'].rolling(window=10, center=True).mean()
z = np.polyfit(df['Year'], df['Temp_Anomaly'], 1)
df['Trend'] = np.polyval(z, df['Year'])

# Make folder if missing
if not os.path.exists('plots/final'):
    os.makedirs('plots/final')

# Plot and save
plt.figure(figsize=(12,6))
plt.plot(df['Year'], df['Temp_Anomaly'], color='lightblue', label='Annual Temp Anomaly')
plt.plot(df['Year'], df['Rolling_Mean'], color='orange', linewidth=2, label='10-Year Rolling Mean')
plt.plot(df['Year'], df['Trend'], color='red', linestyle='--', linewidth=2, label='Trend Line')
plt.xlabel('Year')
plt.ylabel('Temperature Anomaly (°C)')
plt.title('Global Temperature Anomaly Evolution')
plt.grid(alpha=0.3)
plt.legend()
plt.tight_layout()
plt.savefig('plots/final/summary_plot.png', dpi=150)
plt.close()
print("Static summary plot saved at plots/final/summary_plot.png")
