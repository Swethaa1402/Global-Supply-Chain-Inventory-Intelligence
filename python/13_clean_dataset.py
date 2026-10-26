
from pathlib import Path
import pandas as pd

# Locate project folders
project_folder = Path(__file__).resolve().parent.parent

input_file = (
    project_folder
    / "data"
    / "raw"
    / "DataCoSupplyChainDataset.csv"
)

output_folder = project_folder / "data" / "processed"
output_folder.mkdir(parents=True, exist_ok=True)

output_file = output_folder / "supply_chain_cleaned.csv"

# Load original data without modifying it
df = pd.read_csv(input_file, encoding="latin1")

print("Original rows:", len(df))
print("Original columns:", len(df.columns))

# Remove customer-identifying and unnecessary fields
columns_to_remove = [
    "Customer Email",
    "Customer Password",
    "Customer Fname",
    "Customer Lname",
    "Customer Street",
    "Customer Zipcode",
    "Order Zipcode",
    "Product Description",
]

existing_columns = [
    column for column in columns_to_remove
    if column in df.columns
]

df = df.drop(columns=existing_columns)

# Convert date columns to proper datetime format
date_columns = [
    "order date (DateOrders)",
    "shipping date (DateOrders)",
]

for column in date_columns:
    df[column] = pd.to_datetime(df[column], errors="coerce")

# Create delivery delay measure
df["Delivery Delay Days"] = (
    df["Days for shipping (real)"]
    - df["Days for shipment (scheduled)"]
)

# Create a clear delivery timing category
df["Delivery Timing"] = "On Schedule"

df.loc[
    df["Delivery Delay Days"] < 0,
    "Delivery Timing"
] = "Ahead of Schedule"

df.loc[
    df["Delivery Delay Days"] > 0,
    "Delivery Timing"
] = "Delayed"

# Save to processed folder, never overwrite the raw file
df.to_csv(output_file, index=False)

print("\n--- CLEANING SUMMARY ---")
print("Rows after cleaning:", len(df))
print("Columns after cleaning:", len(df.columns))
print("Removed columns:", existing_columns)
print("Missing order dates:", df["order date (DateOrders)"].isna().sum())
print("Missing shipping dates:", df["shipping date (DateOrders)"].isna().sum())
print("Missing delivery delay values:", df["Delivery Delay Days"].isna().sum())

print("\nDelivery timing:")
print(df["Delivery Timing"].value_counts().to_string())

print("\nSaved cleaned dataset to:")
print(output_file)

print("\nOriginal CSV remains unchanged.")
