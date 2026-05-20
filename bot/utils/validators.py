from bot.config.settings import (
    SUPPORTED_ORDER_TYPES,
    SUPPORTED_SIDES
)

from bot.exceptions.custom_exceptions import ValidationError


def validate_symbol(symbol: str) -> str:
    if not symbol:
        raise ValidationError("Symbol cannot be empty")

    return symbol.upper()


def validate_side(side: str) -> str:
    side = side.upper()

    if side not in SUPPORTED_SIDES:
        raise ValidationError(
            f"Invalid side. Supported: {SUPPORTED_SIDES}"
        )

    return side


def validate_order_type(order_type: str) -> str:
    order_type = order_type.upper()

    if order_type not in SUPPORTED_ORDER_TYPES:
        raise ValidationError(
            f"Invalid order type. Supported: {SUPPORTED_ORDER_TYPES}"
        )

    return order_type


def validate_quantity(quantity: float) -> float:
    quantity = float(quantity)

    if quantity <= 0:
        raise ValidationError(
            "Quantity must be greater than 0"
        )

    return quantity


def validate_price(price):
    if price is None:
        raise ValidationError(
            "Price is required for LIMIT orders"
        )

    price = float(price)

    if price <= 0:
        raise ValidationError(
            "Price must be greater than 0"
        )

    return price