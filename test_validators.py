from bot.utils.validators import (
    validate_symbol,
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price
)

print(validate_symbol("btcusdt"))
print(validate_side("buy"))
print(validate_order_type("market"))
print(validate_quantity(0.01))
print(validate_price(50000))