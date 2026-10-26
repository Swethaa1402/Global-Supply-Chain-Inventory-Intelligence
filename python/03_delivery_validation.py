
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

# 1. Compare actual and scheduled shipping durations
df["Shipping Delay Days"] = (
    df["Days for shipping (real)"]
    - df["Days for shipment (scheduled)"]
)

print("\n--- SHIPPING DELAY SUMMARY ---")
print(df["Shipping Delay Days"].describe())

print("\n--- SHIPPING DURATION COMPARISON ---")
print(
    df["Shipping Delay Days"]
    .value_counts()
    .sort_index()
)

# 2. Compare existing risk indicator with delivery status
print("\n--- DELIVERY STATUS ---")
print(df["Delivery Status"].value_counts(dropna=False))

print("\n--- LATE DELIVERY RISK ---")
print(df["Late_delivery_risk"].value_counts(dropna=False))

print("\n--- STATUS VS RISK ---")
print(pd.crosstab(
    df["Delivery Status"],
    df["Late_delivery_risk"],
    margins=True
))

# 3. Validate date parsing without changing the original columns
for col in [
    "order date (DateOrders)",
    "shipping date (DateOrders)"
]:
    parsed = pd.to_datetime(df[col], errors="coerce")

    print(f"\n--- {col} ---")
    print("Unparseable dates:", parsed.isna().sum())
    print("Earliest date:", parsed.min())
    print("Latest date:", parsed.max())

print("\nValidation completed. Original CSV unchanged.")
