
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

market_summary = (
    df.groupby("Market")
    .agg(
        Records=("Shipping Delay Days", "size"),
        Delayed_Records=("Is Delayed", "sum"),
        Average_Delay_Days=("Shipping Delay Days", "mean"),
    )
    .reset_index()
)

market_summary["Delay Rate (%)"] = (
    market_summary["Delayed_Records"]
    / market_summary["Records"]
    * 100
).round(2)

market_summary["Average_Delay_Days"] = (
    market_summary["Average_Delay_Days"].round(2)
)

market_summary = market_summary.sort_values(
    "Delay Rate (%)", ascending=False
)

print("\n--- MARKET DELIVERY PERFORMANCE ---")
print(market_summary.to_string(index=False))

print("\nAnalysis completed. Original CSV unchanged.")
