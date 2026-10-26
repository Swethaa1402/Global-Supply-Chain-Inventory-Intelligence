
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

print("\n--- SALES COLUMN RELATIONSHIPS ---")

print(
    "Sales equals Order Item Total:",
    int((df["Sales"] == df["Order Item Total"]).sum()),
    "of", len(df), "records"
)

print(
    "Sales equals Product Price:",
    int((df["Sales"] == df["Order Item Product Price"]).sum()),
    "of", len(df), "records"
)

print(
    "Order Item Total equals Sales per customer:",
    int((df["Order Item Total"] == df["Sales per customer"]).sum()),
    "of", len(df), "records"
)

print("\n--- SAMPLE ROWS ---")

columns = [
    "Order Id",
    "Order Item Quantity",
    "Order Item Product Price",
    "Order Item Discount",
    "Sales",
    "Order Item Total",
    "Sales per customer",
]

print(df[columns].head(10).to_string(index=False))

print("\n--- CORRELATIONS ---")
print(
    df[
        [
            "Sales",
            "Order Item Total",
            "Sales per customer",
            "Order Item Product Price",
            "Order Item Quantity",
        ]
    ].corr().round(3).to_string()
)

print("\nAnalysis completed. Original CSV unchanged.")
