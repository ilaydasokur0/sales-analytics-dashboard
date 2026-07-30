from services.analysis import load_data  # senin fonksiyonun neyse

sales_df = load_data()

print("\n".join(sales_df.columns))