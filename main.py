import random

import numpy as np

from config import RANDOM_SEED
from generators.customer_generator import generate_customers
from generators.product_generator import generate_products
from generators.invoice_generator import generate_invoices
from generators.detail_generator import generate_invoice_details


def main():
    random.seed(RANDOM_SEED)
    np.random.seed(RANDOM_SEED)

    steps = [
        ("Customers", generate_customers),
        ("Products", generate_products),
        ("Invoices", generate_invoices),
        ("Invoice Details", generate_invoice_details),
    ]

    print("----- DATA GENERATION -----")

    for label, step in steps:
        step()
        print(f"{label} oluşturuldu.")


if __name__ == "__main__":
    main()
