# bot.py
from binance.client import Client
from binance.enums import *
from config import API_KEY, API_SECRET, TESTNET_URL
from logger import setup_logger

logger = setup_logger()

from binance.client import Client
from binance.enums import *

class BasicBot:
    def __init__(self, api_key, api_secret, testnet=True):
        self.client = Client(api_key, api_secret)
        if testnet:
            self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"
        print("Initialized with testnet futures endpoint")

    def place_order(self, symbol, side, order_type, quantity, price=None):
        try:
            logger.info(f"Placing order: {side} {symbol} {quantity} {order_type}")
            if order_type == 'MARKET':
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type=order_type,
                    quantity=quantity
                )
            elif order_type == 'LIMIT':
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type=order_type,
                    timeInForce=TIME_IN_FORCE_GTC,
                    quantity=quantity,
                    price=price
                )
            else:
                raise ValueError("Unsupported order type")
            logger.info(f"Order placed: {order}")
            return order
        except Exception as e:
            logger.error(f"Error placing order: {e}")
            return None