import random
import uuid

import pandas as pd

from constants import PRODUCTS
from paths import data_path


def generate_products():

    products = []

    for product in PRODUCTS:

        product_data = {
            "product_id": str(uuid.uuid4()),
            "product_name": product["name"],
            "product_type": product["type"],
            "unit": product["unit"],
            "pl_status": product["pl_status"]
        }

        products.append(product_data)

    df = pd.DataFrame(products)

    df.to_csv(data_path("products.csv"), index=False)

    return df