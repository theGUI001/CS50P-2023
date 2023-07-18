import sys
import requests


def main():
    argc = len(sys.argv)

    if argc != 2:
        sys.exit("Missing command-line argument")

    try:
        btc_amount_desired = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")
    else:
        pass

    bitcoin_price = get_bitcoin_price()

    if bitcoin_price == "ERROR":
        sys.exit(
            "There was an error getting the current value of Bitcoin. Please try again later"
        )

    price = btc_amount_desired * bitcoin_price

    print(f"${price:,}")


def get_bitcoin_price() -> float or str:
    try:
        r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
    except requests.RequestException:
        return "ERROR"
    else:
        return r["bpi"]["USD"]["rate_float"]


if __name__ == "__main__":
    main()
