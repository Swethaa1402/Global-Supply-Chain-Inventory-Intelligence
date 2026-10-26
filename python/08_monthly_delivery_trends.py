
from pathlib import Path
import pandas as pd

project_folder = Path(__file__).resolve().parent.parent

data_file = (
    project_folder
    / "data"
    / "raw"
    / "DataCoSupplyChainDataset.csv"
)

df = pd.read_csv(data_file, encoding="latin1")

# Parse order dates
df["Order Date"] = pd.to_datetime(
    df["order date (DateOrders)"],
    errors="coerce"
)

# Calculate shipping delay
df["Shipping Delay Days"] = (
    df["Days for shipping (real)"]
    - df["Days for shipment (scheduled)"]
)

# Exclude cancelled records
df = df[df["Delivery Status"] != "Shipping canceled"].copy()

# Remove rows without valid order dates
df = df.dropna(subset=["Order Date"])

# Identify delayed records
df["Is Delayed"] = df["Shipping Delay Days"] > 0

# Create monthly groups
df["Order Month"] = df["Order Date"].dt.to_period("M")

monthly_summary = (
    df.groupby("Order Month")
    .agg(
        Records=("Shipping Delay Days", "size"),
        Delayed_Records=("Is Delayed", "sum"),
        Average_Delay_Days=("Shipping Delay Days", "mean"),
    )
    .reset_index()
)

monthly_summary["Delay Rate (%)"] = (
    monthly_summary["Delayed_Records"]
    / monthly_summary["Records"]
    * 100
).round(2)

monthly_summary["Average_Delay_Days"] = (
    monthly_summary["Average_Delay_Days"].round(2)
)

monthly_summary["Order Month"] = (
    monthly_summary["Order Month"].astype(str)
)

print("\n--- FIRST 12 MONTHS ---")
print(monthly_summary.head(12).to_string(index=False))

print("\n--- 10 MONTHS WITH HIGHEST DELAY RATE ---")
print(
    monthly_summary.nlargest(10, "Delay Rate (%)")
    .to_string(index=False)
)

print("\n--- MONTHLY TREND SUMMARY ---")
print("Months analysed:", len(monthly_summary))
print(
    "Overall delay rate (%):",
    round(df["Is Delayed"].mean() * 100, 2)
)

print("\nAnalysis completed. Original CSV unchanged.")
