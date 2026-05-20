from bot.services.order_service import OrderService


market_order = OrderService.place_market_order(
    symbol="BTCUSDT",
    side="BUY",
    quantity=0.01
)

print("\nMARKET ORDER\n")
print(market_order)


limit_order = OrderService.place_limit_order(
    symbol="BTCUSDT",
    side="BUY",
    quantity=0.01,
    price=50000
)

print("\nLIMIT ORDER\n")
print(limit_order)