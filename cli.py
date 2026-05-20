import typer

from rich.console import Console
from rich.table import Table

from bot.services.order_service import OrderService

from bot.utils.validators import (
    validate_symbol,
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price
)

from bot.utils.logger import logger

app = typer.Typer(
    help="PrimeTrade AI - Simulated Crypto Trading Bot"
)
console = Console()


@app.command()
def trade(
    symbol: str = typer.Option(..., help="Trading pair"),
    side: str = typer.Option(..., help="BUY or SELL"),
    order_type: str = typer.Option(..., "--type", help="MARKET or LIMIT"),
    quantity: float = typer.Option(..., help="Order quantity"),
    price: float = typer.Option(None, help="Limit price")
):
    """
    Execute simulated crypto trades
    """

    try:

        symbol = validate_symbol(symbol)
        side = validate_side(side)
        order_type = validate_order_type(order_type)
        quantity = validate_quantity(quantity)

        if order_type == "LIMIT":
            price = validate_price(price)

        console.print(
            "\n[bold cyan]Processing Order...[/bold cyan]\n"
        )

        if order_type == "MARKET":

            response = OrderService.place_market_order(
                symbol=symbol,
                side=side,
                quantity=quantity
            )

        else:

            response = OrderService.place_limit_order(
                symbol=symbol,
                side=side,
                quantity=quantity,
                price=price
            )

        table = Table(
            title="Order Response",
            show_lines=True
        )

        table.add_column(
            "Field",
            style="bright_cyan",
            justify="left"
        )

        table.add_column(
            "Value",
            style="bright_green",
            justify="left"
        )

        for key, value in response.items():
            table.add_row(
                str(key),
                str(value)
            )

        console.print(table)

        console.print(
            "\n[bold green]Order processed successfully[/bold green]"
        )

    except Exception as error:

        logger.error(f"CLI error: {error}")

        console.print(
            f"\n[bold red]Error:[/bold red] {error}"
        )


if __name__ == "__main__":
    app()