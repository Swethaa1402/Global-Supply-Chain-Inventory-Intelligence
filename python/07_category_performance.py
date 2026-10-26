
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

df["Shipping Delay Days"] = (
    df["Days for shipping (real)"]
    - df["Days for shipment (scheduled)"]
)

# Exclude cancelled records
df = df[df["Delivery Status"] != "Shipping canceled"].copy()

df["Is Delayed"] = df["Shipping Delay Days"] > 0

category_summary = (
    df.groupby("Category Name")
    .agg(
        Records=("Shipping Delay Days", "size"),
        Delayed_Records=("Is Delayed", "sum"),
        Average_Delay_Days=("Shipping Delay Days", "mean"),
    )
    .reset_index()
)

category_summary["Delay Rate (%)"] = (
    category_summary["Delayed_Records"]
    / category_summary["Records"]
    * 100
).round(2)

category_summary["Average_Delay_Days"] = (
    category_summary["Average_Delay_Days"].round(2)
)

category_summary = category_summary.sort_values(
    "Delay Rate (%)", ascending=False
)

print("\n--- PRODUCT CATEGORY DELIVERY PERFORMANCE ---")
print(category_summary.to_string(index=False))

print("\nAnalysis completed. Original CSV unchanged.")
