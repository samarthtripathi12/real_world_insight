# scripts/clean_data.py

import pandas as pd
import os

# -----------------------------
# 1️⃣ Folder paths
# -----------------------------
raw_folder = 'data/raw/'
clean_folder = 'data/clean/'
os.makedirs(clean_folder, exist_ok=True)

# -----------------------------
# 2️⃣ Find CSV
# -----------------------------
csv_files = [f for f in os.listdir(raw_folder) if f.endswith('.csv')]
if not csv_files:
    raise FileNotFoundError(f"No CSV files found in {raw_folder}")

raw_file = os.path.join(raw_folder, csv_files[0])
print(f"Using raw CSV file: {raw_file}")

# -----------------------------
# 3️⃣ Load CSV (skip metadata)
# -----------------------------
# NOAA GLB.Ts+dSST usually has 1 metadata row at top
# Columns: Year, Jan, Feb, ..., Dec, J-D (annual)
df = pd.read_csv(raw_file, skiprows=1)

# Keep only Year and J-D columns
if 'Year' in df.columns and 'J-D' in df.columns:
    df = df[['Year', 'J-D']]
else:
    raise ValueError("CSV does not have expected columns 'Year' and 'J-D'")

# Rename for clarity
df.columns = ['Year', 'Temp_Anomaly']

# Convert to numeric and drop missing
df['Year'] = pd.to_numeric(df['Year'], errors='coerce').astype('Int64')
df['Temp_Anomaly'] = pd.to_numeric(df['Temp_Anomaly'], errors='coerce')
df = df.dropna().reset_index(drop=True)

# -----------------------------
# 4️⃣ Save cleaned CSV
# -----------------------------
clean_file = os.path.join(clean_folder, 'cleaned_temp_anomaly.csv')
df.to_csv(clean_file, index=False)

print(f"✅ Cleaned CSV saved to {clean_file}")
print(f"Final CSV shape: {df.shape}")
