
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

df["Order Date"] = pd.to_datetime(
    df["order date (DateOrders)"],
    errors="coerce"
)

print("\n--- SALES COLUMN VALIDATION ---")

for column in [
    "Sales",
    "Order Item Total",
    "Sales per customer",
    "Order Item Product Price",
]:
    print(f"\n{column}")
    print("Missing values:", df[column].isna().sum())
    print("Total:", round(df[column].sum(), 2))
    print("Minimum:", round(df[column].min(), 2))
    print("Maximum:", round(df[column].max(), 2))

print("\n--- ORDER ITEM COUNTS ---")
items_per_order = df.groupby("Order Id").size()

print("Average rows per order:", round(items_per_order.mean(), 2))
print("Median rows per order:", items_per_order.median())
print("Orders with multiple rows:", int((items_per_order > 1).sum()))

print("\n--- OCTOBER 2017 CHECK ---")
october = df[
    df["Order Date"].dt.to_period("M") == pd.Period("2017-10")
]

print("Records:", len(october))
print("Unique order IDs:", october["Order Id"].nunique())
print(
    "Date range:",
    october["Order Date"].min(),
    "to",
    october["Order Date"].max(),
)
print("Sales total:", round(october["Sales"].sum(), 2))
print(
    "Average Sales per record:",
    round(october["Sales"].mean(), 2),
)

print("\nAnalysis completed. Original CSV unchanged.")
