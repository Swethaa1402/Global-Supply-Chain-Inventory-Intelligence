
from pathlib import Path
import pandas as pd

# Locate and load the original dataset
project_folder = Path(__file__).resolve().parent.parent
data_file = (
    project_folder
    / "data"
    / "raw"
    / "DataCoSupplyChainDataset.csv"
)

df = pd.read_csv(data_file, encoding="latin1")

# Calculate delay relative to scheduled shipping duration
df["Shipping Delay Days"] = (
    df["Days for shipping (real)"]
    - df["Days for shipment (scheduled)"]
)

# Separate cancelled records from other delivery statuses
cancelled = df["Delivery Status"].eq("Shipping canceled")
completed = df.loc[~cancelled].copy()

# Classify performance using the duration fields
completed["Delay Classification"] = "On schedule"
completed.loc[
    completed["Shipping Delay Days"] < 0,
    "Delay Classification"
] = "Ahead of schedule"
completed.loc[
    completed["Shipping Delay Days"] > 0,
    "Delay Classification"
] = "Delayed"

total_records = len(df)
cancelled_records = int(cancelled.sum())
eligible_records = len(completed)

print("\n--- DELIVERY KPI BASELINE ---")
print("Total records:", total_records)
print("Cancelled records:", cancelled_records)
print("Non-cancelled records:", eligible_records)

print("\n--- DELAY CLASSIFICATION ---")
print(completed["Delay Classification"].value_counts())

print("\n--- DELAY CLASSIFICATION (%) ---")
print(
    (completed["Delay Classification"].value_counts(normalize=True) * 100)
    .round(2)
)

print("\n--- AVERAGE SHIPPING DELAY ---")
print(
    "All records:",
    round(df["Shipping Delay Days"].mean(), 2),
    "days"
)
print(
    "Non-cancelled records:",
    round(completed["Shipping Delay Days"].mean(), 2),
    "days"
)

print("\n--- DELIVERY STATUS VS DURATION CLASSIFICATION ---")
print(pd.crosstab(
    completed["Delivery Status"],
    completed["Delay Classification"]
))

print("\n--- LATE DELIVERY RISK VS DURATION ---")
print(pd.crosstab(
    completed["Late_delivery_risk"],
    completed["Delay Classification"]
))

print("\nAnalysis completed. Original CSV unchanged.")
