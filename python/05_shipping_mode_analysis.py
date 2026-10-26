
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

# Calculate delay in days
df["Shipping Delay Days"] = (
    df["Days for shipping (real)"]
    - df["Days for shipment (scheduled)"]
)

# Exclude cancelled records
df = df[df["Delivery Status"] != "Shipping canceled"].copy()

# Identify delayed records
df["Is Delayed"] = df["Shipping Delay Days"] > 0

# Summarise performance by shipping mode
shipping_summary = (
    df.groupby("Shipping Mode")
    .agg(
        Records=("Shipping Delay Days", "size"),
        Delayed_Records=("Is Delayed", "sum"),
        Average_Delay_Days=("Shipping Delay Days", "mean"),
    )
    .reset_index()
)

shipping_summary["Delay Rate (%)"] = (
    shipping_summary["Delayed_Records"]
    / shipping_summary["Records"]
    * 100
).round(2)

shipping_summary["Average_Delay_Days"] = (
    shipping_summary["Average_Delay_Days"].round(2)
)

shipping_summary = shipping_summary.sort_values(
    "Delay Rate (%)", ascending=False
)

print("\n--- SHIPPING MODE PERFORMANCE ---")
print(shipping_summary.to_string(index=False))

print("\nAnalysis completed. Original CSV unchanged.")

