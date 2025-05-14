# cli.py
import argparse
from bot import BasicBot
from config import API_KEY, API_SECRET

def main():
    parser = argparse.ArgumentParser(description="Simplified Binance Futures Trading Bot")
    parser.add_argument('--symbol', type=str, required=True, help='Symbol (e.g. BTCUSDT)')
    parser.add_argument('--side', type=str, required=True, choices=['BUY', 'SELL'])
    parser.add_argument('--type', type=str, required=True, choices=['MARKET', 'LIMIT'])
    parser.add_argument('--quantity', type=float, required=True)
    parser.add_argument('--price', type=float, required=False, help='Price for LIMIT orders')

    args = parser.parse_args()

    bot = BasicBot(API_KEY, API_SECRET)
    order = bot.place_order(args.symbol.upper(), args.side.upper(), args.type.upper(), args.quantity, args.price)
    if order:
        print("Order executed successfully.")
    else:
        print("Order failed.")

if __name__ == '__main__':
    main()