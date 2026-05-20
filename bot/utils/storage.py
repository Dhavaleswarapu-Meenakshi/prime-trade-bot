import json
import os

from bot.utils.logger import logger


ORDERS_FILE = "data/orders.json"


def load_orders():

    if not os.path.exists(ORDERS_FILE):
        return []

    try:

        with open(ORDERS_FILE, "r") as file:
            return json.load(file)

    except Exception as error:

        logger.error(
            f"Failed to load orders: {error}"
        )

        return []


def save_order(order):

    try:

        orders = load_orders()

        orders.append(order)

        with open(ORDERS_FILE, "w") as file:
            json.dump(
                orders,
                file,
                indent=4
            )

        logger.info(
            f"Order saved successfully: {order['orderId']}"
        )

    except Exception as error:

        logger.error(
            f"Failed to save order: {error}"
        )

        raise