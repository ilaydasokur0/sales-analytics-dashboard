import pandas as pd
from config.paths import data_path


def load_data():

    customers = pd.read_csv(data_path("customers.csv"))
    products = pd.read_csv(data_path("products.csv"))
    invoices = pd.read_csv(data_path("invoices.csv"))
    invoice_details = pd.read_csv(data_path("invoice_details.csv"))

    sales_df = (
        invoice_details
        .merge(invoices, on="invoice_id", validate="many_to_one")
        .merge(customers, on="customer_id", validate="many_to_one")
        .merge(products, on="product_id", validate="many_to_one")
    )

    sales_df["invoice_date"] = pd.to_datetime(sales_df["invoice_date"], errors="coerce")

    return sales_df


def filter_data(
    sales_df,
    city=None,
    customer=None,
    product=None,
    start_date=None,
    end_date=None
):

    df = sales_df.copy()

    filters = {
        "city": city,
        "customer_name": customer,
        "product_name": product,
    }

    for column, value in filters.items():
        if value:
            df = df[df[column] == value]

    if start_date:
        df = df[df["invoice_date"] >= pd.to_datetime(start_date)]

    if end_date:
        df = df[df["invoice_date"] <= pd.to_datetime(end_date)]

    return df


# ---------------- KPI ---------------- #

def get_total_sales(df):   #toplam ciro
    return df["total_amount"].sum()


def get_total_invoice_count(df): #toplam fatura sayısı
    return df["invoice_id"].nunique()


def get_total_customer_count(df): #toplam müşteri sayısı
    return df["customer_id"].nunique()


def get_total_product_count(df): #toplam satılan farklı ürün sayısı
    return df["product_id"].nunique()


def get_total_quantity(df): #toplam satılan ürün sayısı
    return df["quantity"].sum()

def get_total_city_count(df):  # satış yapılan il sayısı
    return df["city"].nunique()

def get_average_invoice_amount(df): #ortalama fatura tutarı
    invoice_totals = (
        df.groupby("invoice_id")["total_amount"]
        .sum()
    )

    return 0 if invoice_totals.empty else invoice_totals.mean()


# ---------------- CUSTOMER ---------------- #

# ----- Genel ----- #

def get_top_customers(df, top_n=3):  # en çok alış yapan müşteriler
    return (
        df.groupby("customer_name")["total_amount"]
        .sum()
        .sort_values(ascending=False)
        .head(top_n)
    )


def get_bottom_customers(df, top_n=3):  # en az alış yapan müşteriler
    return (
        df.groupby("customer_name")["total_amount"]
        .sum()
        .sort_values()
        .head(top_n)
    )


# ----- Ciro ----- #

def get_customer_sales(df):  # müşteri bazında toplam ciro
    return (
        df.groupby("customer_name")["total_amount"]
        .sum()
        .sort_values(ascending=False)
    )


def get_customer_share(df):  # müşterilerin toplam satıştaki yüzdesi

    customer_sales = (
        df.groupby("customer_name")["total_amount"]
        .sum()
    )

    total = customer_sales.sum()

    if total == 0:
        return customer_sales * 0

    return ((customer_sales / total) * 100).round(2)


# ----- Ürün ----- #

def get_customer_quantity(df):  # müşteri bazında toplam satış adedi
    return (
        df.groupby("customer_name")["quantity"]
        .sum()
        .sort_values(ascending=False)
    )


def get_customer_top_products(df, top_n=3):  # her müşterinin en çok aldığı ürünler

    customer_products = (
        df.groupby(["customer_name", "product_name"])["quantity"]
        .sum()
        .reset_index()
    )

    return (
        customer_products
        .sort_values(["customer_name", "quantity"], ascending=[True, False])
        .groupby("customer_name")
        .head(top_n)
    )


def get_customer_bottom_products(df, top_n=3):  # her müşterinin en az aldığı ürünler

    customer_products = (
        df.groupby(["customer_name", "product_name"])["quantity"]
        .sum()
        .reset_index()
    )

    return (
        customer_products
        .sort_values(["customer_name", "quantity"], ascending=[True, True])
        .groupby("customer_name")
        .head(top_n)
    )


# ----- Fatura ----- #

def get_customer_invoice_count(df):  # müşteri bazında toplam fatura sayısı
    return (
        df.groupby("customer_name")["invoice_id"]
        .nunique()
        .sort_values(ascending=False)
    )


def get_customer_average_invoice(df):  # müşteri bazında ortalama fatura tutarı

    invoice_totals = (
        df.groupby(["customer_name", "invoice_id"])["total_amount"]
        .sum()
        .reset_index()
    )

    return (
        invoice_totals
        .groupby("customer_name")["total_amount"]
        .mean()
        .sort_values(ascending=False)
    )


# ----- PL ----- #

def get_customer_pl_sales(df):  # müşteri bazında PL cirosu
    return (
        df.groupby(["customer_name", "pl_status"])["total_amount"]
        .sum()
    )


def get_customer_pl_share(df):  # müşteri bazında PL satış yüzdesi

    customer_pl = (
        df.groupby(["customer_name", "pl_status"])["total_amount"]
        .sum()
    )

    totals = customer_pl.groupby(level=0).transform("sum")

    return ((customer_pl / totals.replace(0, pd.NA)) * 100).round(2).fillna(0)


# ----- Ürün Tipi ----- #

def get_customer_product_type_sales(df):  # müşteri bazında ürün tipi cirosu
    return (
        df.groupby(["customer_name", "product_type"])["total_amount"]
        .sum()
    )


def get_customer_product_type_share(df):  # müşteri bazında ürün tipi satış yüzdesi

    customer_type = (
        df.groupby(["customer_name", "product_type"])["total_amount"]
        .sum()
    )

    totals = customer_type.groupby(level=0).transform("sum")

    return ((customer_type / totals.replace(0, pd.NA)) * 100).round(2).fillna(0)

# ---------------- CITY ---------------- #

# ----- Genel ----- #

def get_top_cities(df, top_n=3):  # en çok satış yapılan iller
    return (
        df.groupby("city")["total_amount"]
        .sum()
        .sort_values(ascending=False)
        .head(top_n)
    )


def get_bottom_cities(df, top_n=3):  # en az satış yapılan iller
    return (
        df.groupby("city")["total_amount"]
        .sum()
        .sort_values()
        .head(top_n)
    )


# ----- Ciro ----- #

def get_city_sales(df):  # il bazında toplam ciro
    return (
        df.groupby("city")["total_amount"]
        .sum()
        .sort_values(ascending=False)
    )


def get_city_share(df):  # illerin toplam satıştaki yüzdesi

    city_sales = (
        df.groupby("city")["total_amount"]
        .sum()
    )

    total = city_sales.sum()

    if total == 0:
        return city_sales * 0

    return ((city_sales / total) * 100).round(2)


# ----- Genel Bilgiler ----- #

def get_city_customer_count(df):  # il bazında müşteri sayısı
    return (
        df.groupby("city")["customer_id"]
        .nunique()
        .sort_values(ascending=False)
    )


def get_city_invoice_count(df):  # il bazında fatura sayısı
    return (
        df.groupby("city")["invoice_id"]
        .nunique()
        .sort_values(ascending=False)
    )


def get_city_quantity(df):  # il bazında toplam satış adedi
    return (
        df.groupby("city")["quantity"]
        .sum()
        .sort_values(ascending=False)
    )


def get_city_average_invoice(df):  # il bazında ortalama fatura tutarı

    invoice_totals = (
        df.groupby(["city", "invoice_id"])["total_amount"]
        .sum()
        .reset_index()
    )

    return (
        invoice_totals
        .groupby("city")["total_amount"]
        .mean()
        .sort_values(ascending=False)
    )


# ----- Ürün ----- #

def get_city_top_products(df, top_n=3):  # her ilde en çok satılan ürünler

    city_products = (
        df.groupby(["city", "product_name"])["quantity"]
        .sum()
        .reset_index()
    )

    return (
        city_products
        .sort_values(["city", "quantity"], ascending=[True, False])
        .groupby("city")
        .head(top_n)
    )


def get_city_bottom_products(df, top_n=3):  # her ilde en az satılan ürünler

    city_products = (
        df.groupby(["city", "product_name"])["quantity"]
        .sum()
        .reset_index()
    )

    return (
        city_products
        .sort_values(["city", "quantity"], ascending=[True, True])
        .groupby("city")
        .head(top_n)
    )


# ----- Müşteri ----- #

def get_city_top_customers(df, top_n=3):  # her ilde en çok alış yapan müşteriler

    city_customers = (
        df.groupby(["city", "customer_name"])["total_amount"]
        .sum()
        .reset_index()
    )

    return (
        city_customers
        .sort_values(["city", "total_amount"], ascending=[True, False])
        .groupby("city")
        .head(top_n)
    )


def get_city_bottom_customers(df, top_n=3):  # her ilde en az alış yapan müşteriler

    city_customers = (
        df.groupby(["city", "customer_name"])["total_amount"]
        .sum()
        .reset_index()
    )

    return (
        city_customers
        .sort_values(["city", "total_amount"], ascending=[True, True])
        .groupby("city")
        .head(top_n)
    )


def get_city_average_customer_sales(df):  # il bazında ortalama müşteri cirosu

    customer_sales = (
        df.groupby(["city", "customer_name"])["total_amount"]
        .sum()
        .reset_index()
    )

    return (
        customer_sales
        .groupby("city")["total_amount"]
        .mean()
        .sort_values(ascending=False)
    )


# ----- PL ----- #

def get_city_pl_sales(df):  # il bazında PL cirosu
    return (
        df.groupby(["city", "pl_status"])["total_amount"]
        .sum()
    )


def get_city_pl_quantity(df):  # il bazında PL satış adedi
    return (
        df.groupby(["city", "pl_status"])["quantity"]
        .sum()
    )


def get_city_pl_share(df):  # il bazında PL satış yüzdesi

    city_pl = (
        df.groupby(["city", "pl_status"])["total_amount"]
        .sum()
    )

    totals = city_pl.groupby(level=0).transform("sum")

    return ((city_pl / totals.replace(0, pd.NA)) * 100).round(2).fillna(0)

# ---------------- PRODUCT ---------------- #

# ----- Genel ----- #

def get_product_sales(df):
    return (
        df.groupby("product_name")["total_amount"]
        .sum()
        .sort_values(ascending=False)
    )
# ----- Ciro ----- #

def get_product_share(df):  # ürünlerin toplam satıştaki yüzdesi

    product_sales = (
        df.groupby("product_name")["total_amount"]
        .sum()
    )

    total = product_sales.sum()

    if total == 0:
        return product_sales * 0

    return ((product_sales / total) * 100).round(2)


# ----- Genel Bilgiler ----- #

def get_product_quantity(df):  # ürün bazında toplam satış adedi
    return (
        df.groupby("product_name")["quantity"]
        .sum()
        .sort_values(ascending=False)
    )


def get_product_invoice_count(df):  # ürün bazında fatura sayısı
    return (
        df.groupby("product_name")["invoice_id"]
        .nunique()
        .sort_values(ascending=False)
    )


# ----- Müşteri ----- #

def get_product_top_customers(df, top_n=3):  # ürünü en çok alan müşteriler

    product_customers = (
        df.groupby(["product_name", "customer_name"])["quantity"]
        .sum()
        .reset_index()
    )

    return (
        product_customers
        .sort_values(["product_name", "quantity"], ascending=[True, False])
        .groupby("product_name")
        .head(top_n)
    )


def get_product_bottom_customers(df, top_n=3):  # ürünü en az alan müşteriler

    product_customers = (
        df.groupby(["product_name", "customer_name"])["quantity"]
        .sum()
        .reset_index()
    )

    return (
        product_customers
        .sort_values(["product_name", "quantity"], ascending=[True, True])
        .groupby("product_name")
        .head(top_n)
    )


# ----- İl ----- #

def get_product_top_cities(df, top_n=3):  # ürünün en çok satıldığı iller

    product_cities = (
        df.groupby(["product_name", "city"])["quantity"]
        .sum()
        .reset_index()
    )

    return (
        product_cities
        .sort_values(["product_name", "quantity"], ascending=[True, False])
        .groupby("product_name")
        .head(top_n)
    )


def get_product_bottom_cities(df, top_n=3):  # ürünün en az satıldığı iller

    product_cities = (
        df.groupby(["product_name", "city"])["quantity"]
        .sum()
        .reset_index()
    )

    return (
        product_cities
        .sort_values(["product_name", "quantity"], ascending=[True, True])
        .groupby("product_name")
        .head(top_n)
    )

# ---------------- DATE ---------------- #

def get_daily_sales(df):  # günlük toplam ciro
    return (
        df.groupby(df["invoice_date"].dt.date)["total_amount"]
        .sum()
    )


def get_weekly_sales(df):  # haftalık toplam ciro

    weekly = df.copy()

    weekly["year_week"] = weekly["invoice_date"].dt.strftime("%G-W%V")

    return (
        weekly.groupby("year_week")["total_amount"]
        .sum()
    )


def get_monthly_sales(df):  # aylık toplam ciro

    monthly = df.copy()

    monthly["year_month"] = monthly["invoice_date"].dt.to_period("M").astype(str)

    return (
        monthly.groupby("year_month")["total_amount"]
        .sum()
    )

def get_daily_quantity(df):  # günlük satılan ürün adedi
    return (
        df.groupby(df["invoice_date"].dt.date)["quantity"]
        .sum()
    )


def get_weekly_quantity(df):  # haftalık satılan ürün adedi

    weekly = df.copy()

    weekly["year_week"] = weekly["invoice_date"].dt.strftime("%G-W%V")

    return (
        weekly.groupby("year_week")["quantity"]
        .sum()
    )


def get_monthly_quantity(df):  # aylık satılan ürün adedi

    monthly = df.copy()

    monthly["year_month"] = monthly["invoice_date"].dt.to_period("M").astype(str)

    return (
        monthly.groupby("year_month")["quantity"]
        .sum()
    )
