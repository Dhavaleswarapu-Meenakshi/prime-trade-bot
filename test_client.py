from bot.api.client import BinanceClient

data = BinanceClient.get_market_price("BTCUSDT")

print(data)