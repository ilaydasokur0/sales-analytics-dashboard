import random
import uuid

import numpy as np
import pandas as pd

from config import (
    MIN_PRODUCTS_PER_INVOICE,
    MAX_PRODUCTS_PER_INVOICE
)
from paths import data_path


def generate_invoice_details():

    invoices = pd.read_csv(data_path("invoices.csv"))
    products = pd.read_csv(data_path("products.csv"))

    # Ensure invoices are processed in chronological order so repeats reflect time
    invoices["invoice_date"] = pd.to_datetime(invoices["invoice_date"], errors="coerce")
    invoices = invoices.sort_values("invoice_date").reset_index(drop=True)

    # Assign a popularity score and repeatability factor to products (internal only)
    rng = np.random.default_rng()
    # popularity: skewed so few products are very popular
    popularity = rng.gamma(2.0, 1.0, size=len(products))
    # repeatability: beta distribution so some products rarely repeat
    repeatability = rng.beta(2.0, 5.0, size=len(products))

    products = products.reset_index(drop=True)
    products["popularity"] = popularity
    products["repeatability"] = repeatability

    product_ids = products["product_id"].tolist()
    product_pop = products["popularity"].to_numpy()
    product_rep = products["repeatability"].to_numpy()

    # Track previous purchases per customer to encourage repeats
    customer_history = {}

    invoice_details = []

    for _, invoice in invoices.iterrows():

        product_count = random.randint(
            MIN_PRODUCTS_PER_INVOICE,
            MAX_PRODUCTS_PER_INVOICE
        )

        cust_id = invoice["customer_id"]

        # Build weights: base popularity, boosted if customer has bought before (and product repeatability)
        base_weights = product_pop.copy().astype(float)

        if cust_id in customer_history and customer_history[cust_id]:
            bought_set = set(customer_history[cust_id])
            # boost previously bought products by a factor scaled by their repeatability
            for idx, pid in enumerate(product_ids):
                if pid in bought_set:
                    base_weights[idx] += product_rep[idx] * 3.0

        # Normalize to probabilities
        if base_weights.sum() <= 0:
            probs = np.repeat(1.0 / len(base_weights), len(base_weights))
        else:
            probs = base_weights / base_weights.sum()

        # Sample products for this invoice without replacement using probabilities
        # ensure product_count does not exceed available products
        k = min(product_count, len(product_ids))
        try:
            selected_indices = rng.choice(len(product_ids), size=k, replace=False, p=probs)
        except Exception:
            # fallback to uniform sample if probabilities problematic
            selected_indices = rng.choice(len(product_ids), size=k, replace=False)

        selected_products = products.loc[selected_indices]

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

            # update customer history
            customer_history.setdefault(cust_id, []).append(product["product_id"])

    df = pd.DataFrame(invoice_details)

    df.to_csv(data_path("invoice_details.csv"), index=False)

    return df