import pandas as pd

df = pd.read_csv("data/invoice_details.csv")
print(df.head(20).to_string())