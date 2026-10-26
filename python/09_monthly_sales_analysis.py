
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

df = df.dropna(subset=["Order Date"]).copy()

df["Order Month"] = df["Order Date"].dt.to_period("M")

monthly_sales = (
    df.groupby("Order Month")
    .agg(
        Records=("Order Id", "size"),
        Unique_Orders=("Order Id", "nunique"),
        Total_Sales=("Sales", "sum"),
        Average_Sales_Per_Record=("Sales", "mean"),
    )
    .reset_index()
)

monthly_sales["Total_Sales"] = (
    monthly_sales["Total_Sales"].round(2)
)

monthly_sales["Average_Sales_Per_Record"] = (
    monthly_sales["Average_Sales_Per_Record"].round(2)
)

monthly_sales["Order Month"] = (
    monthly_sales["Order Month"].astype(str)
)

print("\n--- FIRST 12 MONTHS OF SALES ---")
print(monthly_sales.head(12).to_string(index=False))

print("\n--- TOP 10 MONTHS BY TOTAL SALES ---")
print(
    monthly_sales.nlargest(10, "Total_Sales")
    .to_string(index=False)
)

print("\n--- SALES ANALYSIS SUMMARY ---")
print("Months analysed:", len(monthly_sales))
print("Total records:", len(df))
print("Unique order IDs:", df["Order Id"].nunique())
print("Total Sales:", round(df["Sales"].sum(), 2))

print("\nAnalysis completed. Original CSV unchanged.")
