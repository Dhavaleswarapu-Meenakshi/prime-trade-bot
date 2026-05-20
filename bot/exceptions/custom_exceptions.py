class TradingBotError(Exception):
    """
    Base exception class
    """
    pass


class ValidationError(TradingBotError):
    """
    Raised for validation errors
    """
    pass


class APIError(TradingBotError):
    """
    Raised for API-related errors
    """
    pass


class OrderExecutionError(TradingBotError):
    """
    Raised when order execution fails
    """
    pass