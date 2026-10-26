
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

expected_total = (
    df["Order Item Product Price"] * df["Order Item Quantity"]
    - df["Order Item Discount"]
)

difference = (
    df["Order Item Total"] - expected_total
).abs()

print("\n--- ITEM TOTAL VALIDATION ---")

print("Records checked:", len(df))
print(
    "Records matching formula within 0.02:",
    int((difference <= 0.02).sum())
)
print(
    "Records not matching formula within 0.02:",
    int((difference > 0.02).sum())
)
print("Maximum absolute difference:", round(difference.max(), 4))

print("\n--- SAMPLE MISMATCHES ---")

mismatch_columns = [
    "Order Id",
    "Order Item Quantity",
    "Order Item Product Price",
    "Order Item Discount",
    "Order Item Total",
]

print(
    df.loc[difference > 0.02, mismatch_columns]
    .head(10)
    .to_string(index=False)
)

print("\nValidation completed. Original CSV unchanged.")
