import random
import uuid
from datetime import datetime, timedelta

import pandas as pd

from config import INVOICE_COUNT, START_DATE, END_DATE
from paths import data_path


def generate_invoices():

    customers = pd.read_csv(data_path("customers.csv"))

    start_date = datetime.strptime(START_DATE, "%Y-%m-%d")
    end_date = datetime.strptime(END_DATE, "%Y-%m-%d")

    date_difference = (end_date - start_date).days

    invoices = []

    for i in range(INVOICE_COUNT):

        customer = customers.sample(1).iloc[0]

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