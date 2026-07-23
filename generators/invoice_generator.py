import random
import uuid
from datetime import datetime, timedelta

import numpy as np
import pandas as pd

from config.config import INVOICE_COUNT, START_DATE, END_DATE
from config.paths import data_path


def generate_invoices():

    customers = pd.read_csv(data_path("customers.csv"))

    start_date = datetime.strptime(START_DATE, "%Y-%m-%d")
    end_date = datetime.strptime(END_DATE, "%Y-%m-%d")

    date_difference = (end_date - start_date).days

    # Assign per-customer invoice frequency weights so some customers are more frequent buyers
    # We sample weights from a gamma distribution to create variability
    customer_weights = np.random.default_rng().gamma(shape=2.0, scale=1.0, size=len(customers))

    # Sample customers for each invoice according to weights (with replacement)
    sampled_customers = customers.sample(n=INVOICE_COUNT, replace=True, weights=customer_weights)
    sampled_customers = sampled_customers.reset_index(drop=True)

    invoices = []

    for i in range(INVOICE_COUNT):
        customer = sampled_customers.iloc[i]

        random_days = random.randint(0, date_difference)
        invoice_date = start_date + timedelta(days=random_days)

        invoice = {
            "invoice_id": str(uuid.uuid4()),
            "invoice_number": f"K{2025}{i + 1:06}",
            "customer_id": customer["customer_id"],
            "invoice_date": invoice_date.strftime("%Y-%m-%d")
        }

        invoices.append(invoice)

    df = pd.DataFrame(invoices)

    df.to_csv(data_path("invoices.csv"), index=False)

    return df

if __name__ == "__main__":
    generate_invoices()