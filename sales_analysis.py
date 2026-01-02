import pandas as pd

# Load dataset
df = pd.read_csv("sales_data.csv")

# Handle missing values
df.fillna(0, inplace=True)

# --- Calculations ---
total_sales = df["Sales"].sum()
best_selling_product = df.groupby("Product")["Sales"].sum().idxmax()
average_sales = df["Sales"].mean()
total_orders = len(df)

# --- Print Results ---
print("---- Sales Analysis Report ----")
print(f"Total Sales: {total_sales}")
print(f"Best Selling Product: {best_selling_product}")
print(f"Average Sales Per Order: {average_sales}")
print(f"Total Orders: {total_orders}")
