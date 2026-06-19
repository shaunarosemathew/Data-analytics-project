import pandas as pd
df = pd.read_csv("file.csv")
print(df.head())

df.tail()
df.info()
df.describe()
print(df.isnull().sum())
df.drop("Unnamed: 0", axis=1, inplace=True, errors="ignore")
df["Gender"] = df["Gender"].fillna(df["Gender"].mode()[0])
print(df.isnull().sum())
df["Location"] = df["Location"].fillna(df["Location"].mode()[0])
df["CustomerID"] = df["CustomerID"].fillna("Unknown")
df["Transaction_ID"] = df["Transaction_ID"].fillna("Unknown")

df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")
df["Avg_Price"] = pd.to_numeric(df["Avg_Price"], errors="coerce")
df["Discount_pct"] = pd.to_numeric(df["Discount_pct"], errors="coerce")

df["Quantity"] = df["Quantity"].fillna(df["Quantity"].median())
df["Avg_Price"] = df["Avg_Price"].fillna(df["Avg_Price"].mean())
df["Discount_pct"] = df["Discount_pct"].fillna(0)

df["Coupon_Code"] = df["Coupon_Code"].fillna("No Coupon")

df["Transaction_Date"] = pd.to_datetime(
    df["Transaction_Date"],
    errors="coerce"
)

df.drop_duplicates(inplace=True)

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

print("\nDataset Shape:")
print(df.shape)

df.to_csv("cleaned_ecommerce_data.csv", index=False)

print("\nData cleaned and saved successfully!")

