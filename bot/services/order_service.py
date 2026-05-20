import uuid
from datetime import datetime
from bot.utils.storage import save_order
from bot.api.client import BinanceClient
from bot.utils.logger import logger


class OrderService:

    @staticmethod
    def place_market_order(
        symbol,
        side,
        quantity
    ):

        market_data = BinanceClient.get_market_price(symbol)

        current_price = market_data["price"]

        executed_value = round(
            current_price * quantity,
            2
        )

        order_response = {
            "orderId": str(uuid.uuid4())[:8],
            "symbol": symbol,
            "side": side,
            "type": "MARKET",
            "status": "FILLED",
            "price": current_price,
            "executedQty": quantity,
            "executedValue": executed_value,
            "timestamp": datetime.utcnow().isoformat()
        }

        logger.info(
            f"MARKET order executed: {order_response}"
        )
        save_order(order_response)
        return order_response

    @staticmethod
    def place_limit_order(
        symbol,
        side,
        quantity,
        price
    ):

        market_data = BinanceClient.get_market_price(symbol)

        current_price = market_data["price"]

        if side == "BUY":
            status = (
                "FILLED"
                if current_price <= price
                else "OPEN"
            )

        else:
            status = (
                "FILLED"
                if current_price >= price
                else "OPEN"
            )
        executed_value = round(
            price * quantity,
            2
        )

        order_response = {
            "orderId": str(uuid.uuid4())[:8],
            "symbol": symbol,
            "side": side,
            "type": "LIMIT",
            "status": status,
            "price": price,
            "marketPrice": current_price,
            "executedQty": quantity,
            "executedValue": executed_value,
            "timestamp": datetime.utcnow().isoformat()
        }

        logger.info(
            f"LIMIT order processed: {order_response}"
        )
        save_order(order_response)
        return order_response