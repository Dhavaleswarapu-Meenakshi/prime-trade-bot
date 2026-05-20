import requests
from bot.exceptions.custom_exceptions import APIError
from bot.config.settings import (
    BINANCE_BASE_URL,
    DEFAULT_TIMEOUT
)

from bot.utils.logger import logger


class BinanceClient:

    @staticmethod
    def get_market_price(symbol: str):
        """
        Fetch live market price from Binance public API
        """

        endpoint = f"{BINANCE_BASE_URL}/api/v3/ticker/price"

        params = {
            "symbol": symbol.upper()
        }

        try:
            logger.info(
                f"Fetching market price for {symbol}"
            )

            response = requests.get(
                endpoint,
                params=params,
                timeout=DEFAULT_TIMEOUT
            )

            response.raise_for_status()

            data = response.json()

            logger.info(
                f"Market data received: {data}"
            )

            return {
                "symbol": data["symbol"],
                "price": float(data["price"])
            }

        except requests.exceptions.Timeout:
            logger.error("Request timed out")
            raise APIError(
                "Binance API request timed out"
            )

        except requests.exceptions.ConnectionError:
            logger.error("Connection error")
            raise APIError(
                "Failed to connect to Binance API"
            )

        except requests.exceptions.HTTPError as error:
            logger.error(f"HTTP error: {error}")
            raise APIError(
                "Binance API returned an error"
            )

        except Exception as error:
            logger.error(f"Unexpected error: {error}")
            raise