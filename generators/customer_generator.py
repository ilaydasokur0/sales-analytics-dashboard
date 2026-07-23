import random
import uuid

import pandas as pd

from config.config import CUSTOMER_COUNT
from config.constants import CUSTOMER_NAMES, CITIES
from config.paths import data_path


def generate_customers():

    customers = []

    selected_names = random.sample(CUSTOMER_NAMES, CUSTOMER_COUNT)

    for customer_name in selected_names:

        customer = {
            "customer_id": str(uuid.uuid4()),
            "customer_name": customer_name,
            "city": random.choice(CITIES)
        }

        customers.append(customer)

    df = pd.DataFrame(customers)

    df.to_csv(data_path("customers.csv"), index=False)

    return df

if __name__ == "__main__":
    generate_customers()