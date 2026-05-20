import json
import pandas as pd
import streamlit as st
from streamlit_autorefresh import st_autorefresh
from bot.api.client import BinanceClient
from bot.services.order_service import OrderService

from bot.utils.validators import (
    validate_symbol,
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price
)


st.set_page_config(
    page_title="PrimeTrade AI Bot",
    layout="wide"
)

st.title("🚀 PrimeTrade AI - Trading Dashboard")
st_autorefresh(
    interval=15000,
    key="market_refresh"
)

# Sidebar
st.sidebar.header("Order Configuration")

symbol = st.sidebar.text_input(
    "Symbol",
    value="BTCUSDT"
)

side = st.sidebar.selectbox(
    "Side",
    ["BUY", "SELL"]
)

order_type = st.sidebar.selectbox(
    "Order Type",
    ["MARKET", "LIMIT"]
)

quantity = st.sidebar.number_input(
    "Quantity",
    min_value=0.001,
    value=0.01
)

price = None

if order_type == "LIMIT":

    price = st.sidebar.number_input(
        "Limit Price",
        min_value=0.01,
        value=70000.0
    )


# Live Market Price
st.subheader("📈 Live Market Data")

try:

    market_data = BinanceClient.get_market_price(symbol)

    st.metric(
        label=f"{symbol} Price",
        value=f"${market_data['price']:,.2f}"
    )

except Exception as error:

    st.error(
        f"Failed to fetch market data: {error}"
    )


# Execute Order
if st.sidebar.button("Execute Order"):

    try:

        symbol = validate_symbol(symbol)
        side = validate_side(side)
        order_type = validate_order_type(order_type)
        quantity = validate_quantity(quantity)

        if order_type == "LIMIT":
            price = validate_price(price)

        if order_type == "MARKET":

            response = OrderService.place_market_order(
                symbol,
                side,
                quantity
            )

        else:

            response = OrderService.place_limit_order(
                symbol,
                side,
                quantity,
                price
            )

        st.success("Order processed successfully")

        st.json(response)

    except Exception as error:

        st.error(str(error))
# Dashboard Metrics
try:

    with open("data/orders.json", "r") as file:

        orders = json.load(file)

    total_orders = len(orders)

    filled_orders = len([
        order for order in orders
        if order.get("status") == "FILLED"
    ])

    open_orders = len([
        order for order in orders
        if order.get("status") == "OPEN"
    ])

    total_value = sum([
        float(order.get("executedValue", 0))
        for order in orders
    ])

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Total Orders",
        total_orders
    )

    col2.metric(
        "Filled Orders",
        filled_orders
    )

    col3.metric(
        "Open Orders",
        open_orders
    )

    col4.metric(
        "Total Traded Value",
        f"${total_value:,.2f}"
    )

except Exception:
    pass

# Order History
st.subheader("📜 Order History")

try:

    with open("data/orders.json", "r") as file:

        orders = json.load(file)

    if orders:

        df = pd.DataFrame(orders)

        st.dataframe(
            df,
            use_container_width=True
        )

    else:

        st.info("No orders available")

except Exception as error:

    st.error(
        f"Failed to load order history: {error}"
    )
st.markdown("---")

st.caption(
    "PrimeTrade AI Internship Assessment Project | Python Trading Bot Dashboard"
)