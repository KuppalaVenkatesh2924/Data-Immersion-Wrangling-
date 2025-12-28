import pandas as pd
from datetime import datetime

df = pd.read_excel("../data/raw_data.xlsx")

df.drop_duplicates(inplace=True)
df["purchase_amount"].fillna(df["purchase_amount"].median(), inplace=True)
df["dob"].fillna("1999-01-01", inplace=True)

df["dob"] = pd.to_datetime(df["dob"])
df["signup_date"] = pd.to_datetime(df["signup_date"])

current_year = datetime.now().year
df["customer_age"] = current_year - df["dob"].dt.year

df["city"] = df["city"].str.title()

df.to_excel("../data/cleaned_data.xlsx", index=False)

print("Data cleaning completed successfully")
