import random
import uuid

import pandas as pd

from config import (
    MIN_PRODUCTS_PER_INVOICE,
    MAX_PRODUCTS_PER_INVOICE
)
from paths import data_path


def generate_invoice_details():

    invoices = pd.read_csv(data_path("invoices.csv"))
    products = pd.read_csv(data_path("products.csv"))

    invoice_details = []

    for _, invoice in invoices.iterrows():

        product_count = random.randint(
            MIN_PRODUCTS_PER_INVOICE,
            MAX_PRODUCTS_PER_INVOICE
        )

        selected_products = products.sample(product_count)

        for _, product in selected_products.iterrows():

            quantity = random.randint(1, 100)

            unit_price = random.randint(50, 1000)

            total_amount = quantity * unit_price

            detail = {
                "detail_id": str(uuid.uuid4()),
                "invoice_id": invoice["invoice_id"],
                "product_id": product["product_id"],
                "quantity": quantity,
                "unit_price": unit_price,
                "total_amount": total_amount
            }

            invoice_details.append(detail)

    df = pd.DataFrame(invoice_details)

    df.to_csv(data_path("invoice_details.csv"), index=False)

    return df