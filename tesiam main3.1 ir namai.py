import pandas as pd


file_path = "namai.csv"
products_df = pd.read_csv(file_path)

products_df['Price'] = products_df['Price'].replace('N/A', pd.NA)
products_df['Price'] = products_df['Price'].astype(str)

products_df['Price'] = products_df['Price'].apply(lambda x: float(x) if pd.notna(x) and x else x)

print(products_df)