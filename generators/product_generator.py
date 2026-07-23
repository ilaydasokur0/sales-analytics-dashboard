import random
import uuid

import pandas as pd

from config.constants import PRODUCTS
from config.paths import data_path


def generate_products():

    products = []

    for product in PRODUCTS:

        product_data = {
            "product_id": str(uuid.uuid4()),
            "product_name": product["name"],
            "product_type": product["type"],
            "pl_status": product["pl_status"]
        }

        products.append(product_data)

    df = pd.DataFrame(products)

    df.to_csv(data_path("products.csv"), index=False)

    return df

if __name__ == "__main__":
    generate_products()