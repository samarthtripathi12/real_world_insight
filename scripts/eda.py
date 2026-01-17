# scripts/eda.py

import pandas as pd
import matplotlib.pyplot as plt
import os
from matplotlib.animation import FuncAnimation, PillowWriter

# -----------------------------
# 1️⃣ Folder paths
# -----------------------------
clean_folder = 'data/clean/'
output_folder = 'outputs/'
os.makedirs(output_folder, exist_ok=True)

clean_file = os.path.join(clean_folder, 'cleaned_temp_anomaly.csv')

# -----------------------------
# 2️⃣ Load cleaned CSV
# -----------------------------
df = pd.read_csv(clean_file)
print(f"Loaded cleaned CSV: {df.shape} rows, {df.shape[1]} columns")

# -----------------------------
# 3️⃣ Basic line plot: Temperature over years
# -----------------------------
plt.figure(figsize=(10,5))
plt.plot(df['Year'], df['Temp_Anomaly'], color='red', label='Temp Anomaly (°C)')
plt.xlabel('Year')
plt.ylabel('Temperature Anomaly (°C)')
plt.title('Global Temperature Anomaly Over Time')
plt.grid(True)
plt.legend()
plt.tight_layout()
line_plot_file = os.path.join(output_folder, 'temp_anomaly_line.png')
plt.savefig(line_plot_file)
plt.close()
print(f"Saved line plot: {line_plot_file}")

# -----------------------------
# 4️⃣ Histogram of temperature anomalies
# -----------------------------
plt.figure(figsize=(8,5))
plt.hist(df['Temp_Anomaly'], bins=20, color='orange', edgecolor='black')
plt.xlabel('Temperature Anomaly (°C)')
plt.ylabel('Frequency')
plt.title('Histogram of Global Temperature Anomalies')
plt.grid(axis='y')
plt.tight_layout()
hist_file = os.path.join(output_folder, 'temp_anomaly_hist.png')
plt.savefig(hist_file)
plt.close()
print(f"Saved histogram: {hist_file}")

# -----------------------------
# 5️⃣ Rolling mean (10-year)
# -----------------------------
df['Rolling_Mean_10'] = df['Temp_Anomaly'].rolling(window=10).mean()

plt.figure(figsize=(10,5))
plt.plot(df['Year'], df['Temp_Anomaly'], color='red', alpha=0.5, label='Temp Anomaly')
plt.plot(df['Year'], df['Rolling_Mean_10'], color='blue', label='10-Year Rolling Mean')
plt.xlabel('Year')
plt.ylabel('Temperature Anomaly (°C)')
plt.title('Temperature Anomaly with 10-Year Rolling Mean')
plt.legend()
plt.grid(True)
plt.tight_layout()
rolling_file = os.path.join(output_folder, 'rolling_mean.png')
plt.savefig(rolling_file)
plt.close()
print(f"Saved rolling mean plot: {rolling_file}")

# -----------------------------
# 6️⃣ Animated GIF: Temperature over time
# -----------------------------
fig, ax = plt.subplots(figsize=(10,5))
ax.set_xlim(df['Year'].min(), df['Year'].max())
ax.set_ylim(df['Temp_Anomaly'].min()-0.1, df['Temp_Anomaly'].max()+0.1)
ax.set_xlabel('Year')
ax.set_ylabel('Temperature Anomaly (°C)')
ax.set_title('Global Temperature Anomaly Over Time')
line, = ax.plot([], [], color='red')

xdata, ydata = [], []

def animate(i):
    xdata.append(df['Year'].iloc[i])
    ydata.append(df['Temp_Anomaly'].iloc[i])
    line.set_data(xdata, ydata)
    return line,

ani = FuncAnimation(fig, animate, frames=len(df), interval=100, blit=True)
gif_file = os.path.join(output_folder, 'temp_anomaly_animation.gif')
ani.save(gif_file, writer=PillowWriter(fps=10))
plt.close()
print(f"Saved animated GIF: {gif_file}")

print("✅ Phase 3 (EDA) complete. All outputs saved in 'outputs/' folder.")
