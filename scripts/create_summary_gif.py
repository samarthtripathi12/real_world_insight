import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import os  # for folder checks

# -------------------------------
# Step 0: Ensure output folder exists
# -------------------------------
if not os.path.exists('gifs'):
    os.makedirs('gifs')  # creates the gifs folder if missing

# -------------------------------
# Step 1: Load cleaned dataset
# -------------------------------
df = pd.read_csv('data/clean/cleaned_temp_anomaly.csv')  # use your cleaned CSV
# Check columns
if 'Year' not in df.columns or 'Temp_Anomaly' not in df.columns:
    raise ValueError("CSV must have 'Year' and 'Temp_Anomaly' columns")

# -------------------------------
# Step 2: Compute rolling mean and trend
# -------------------------------
df['Rolling_Mean'] = df['Temp_Anomaly'].rolling(window=10, center=True).mean()
z = np.polyfit(df['Year'], df['Temp_Anomaly'], 1)
df['Trend'] = np.polyval(z, df['Year'])

# -------------------------------
# Step 3: Setup plot
# -------------------------------
fig, ax = plt.subplots(figsize=(12,6))
ax.set_xlim(df['Year'].min(), df['Year'].max())
ax.set_ylim(df['Temp_Anomaly'].min()-0.1, df['Temp_Anomaly'].max()+0.1)
ax.set_xlabel('Year')
ax.set_ylabel('Temperature Anomaly (°C)')
ax.set_title('Global Temperature Anomaly Evolution')
ax.grid(alpha=0.3)

# Initialize lines
line_raw, = ax.plot([], [], color='lightblue', label='Annual Temp Anomaly')
line_roll, = ax.plot([], [], color='orange', linewidth=2, label='10-Year Rolling Mean')
line_trend, = ax.plot([], [], color='red', linestyle='--', linewidth=2, label='Trend Line')
ax.legend()

# -------------------------------
# Step 4: Animation function
# -------------------------------
def animate(i):
    x = df['Year'][:i]
    y_raw = df['Temp_Anomaly'][:i]
    y_roll = df['Rolling_Mean'][:i]
    y_trend = df['Trend'][:i]
    
    line_raw.set_data(x, y_raw)
    line_roll.set_data(x, y_roll)
    line_trend.set_data(x, y_trend)
    
    return line_raw, line_roll, line_trend

# -------------------------------
# Step 5: Create and save GIF
# -------------------------------
ani = FuncAnimation(fig, animate, frames=len(df), interval=50, blit=True)
ani.save('gifs/insight_evolution.gif', writer='pillow', dpi=150)
plt.close()

print("GIF successfully created at gifs/insight_evolution.gif")

