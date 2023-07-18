from tkinter import Tk, Canvas, PhotoImage, Button, Entry
import requests
from datetime import datetime
import pandas as pd
import mplfinance as mpf
from PIL import Image, ImageTk

VALID_TICKERS = requests.get("https://brapi.dev/api/available").json()["stocks"]


def array_to_data_frame(arr: list):
    for obj in arr:
        obj["date"] = timestamp_to_date(obj["date"])

    df = pd.DataFrame(arr)
    df = df.set_index("date")
    df.index = pd.to_datetime(df.index)
    df.index.name = "Date"
    return df


def timestamp_to_date(timestamp: int):
    return datetime.utcfromtimestamp(timestamp).date()


def format_to_brl(value: float) -> str:
    if value >= 1e12:
        value_str = f"{value / 1e12:,.2f} Tri"
    elif value >= 1e9:
        value_str = f"{value / 1e9:,.2f} Bi"
    elif value >= 1e6:
        value_str = f"{value / 1e6:,.2f} Mi"
    elif value >= 1e3:
        value_str = f"{value / 1e3:,.2f} K"
    else:
        value_str = f"{value:,.2f}"
    return f"R$ {value_str}".replace(",", "X").replace(".", ",").replace("X", ".")


def get_info(ticker: str):
    if ticker in VALID_TICKERS:
        return (
            requests.get(
                f"https://brapi.dev/api/quote/{ticker}?range=3mo&interval=1d&fundamental=true"
            )
            .json()["results"]
            .pop()
        )
    else:
        pass


def main():
    ticker = get_info("BBAS3")

    def update_chart():
        nonlocal ticker, df, fig, chart_image, canvas, chart
        df = array_to_data_frame(ticker["historicalDataPrice"])
        fig = mpf.plot(
            df,
            type="candle",
            mav=(20),
            volume=True,
            style=my_style,
            savefig=dict(fname="chart.png", transparent=True),
            figsize=(10, 3),
            xlabel="",
            ylabel="",
            ylabel_lower="",
        )
        chart_image = ImageTk.PhotoImage(Image.open("chart.png"))
        canvas.itemconfig(chart, image=chart_image)

    def update_ticker(*args):
        nonlocal ticker, canvas, symbol, price, market_cap, low_value, high_value, volume
        ticker = get_info(entry0.get().upper())
        entry0.delete(0, "end")
        canvas.itemconfig(symbol, text=ticker["symbol"])
        canvas.itemconfig(price, text=format_to_brl(ticker["regularMarketPrice"]))
        canvas.itemconfig(low_value, text=format_to_brl(ticker["fiftyTwoWeekLow"]))
        canvas.itemconfig(high_value, text=format_to_brl(ticker["fiftyTwoWeekHigh"]))
        canvas.itemconfig(
            volume, text=format_to_brl(ticker["averageDailyVolume3Month"])
        )
        if "marketCap" in ticker:
            canvas.itemconfig(market_cap, text=format_to_brl(ticker["marketCap"]))
        else:
            canvas.itemconfig(market_cap, text="---")

        update_chart()

    df = array_to_data_frame(ticker["historicalDataPrice"])

    window = Tk()

    window.title("Py Finance")
    window.geometry("1086x611")
    window.configure(bg="#111827")
    canvas = Canvas(
        window,
        bg="#111827",
        height=611,
        width=1086,
        bd=0,
        highlightthickness=0,
        relief="ridge",
    )
    canvas.place(x=0, y=0)

    background_img = PhotoImage(file=f"background.png")
    background = canvas.create_image(543.0, 305.5, image=background_img)

    my_style = mpf.make_mpf_style(
        facecolor="none",
        base_mpf_style="yahoo",
        rc={
            "text.color": "white",
            "axes.labelcolor": "white",
            "xtick.color": "white",
            "ytick.color": "white",
        },
    )

    fig = mpf.plot(
        df,
        type="candle",
        mav=(20),
        volume=True,
        style=my_style,
        savefig=dict(fname="chart.png", transparent=True),
        figsize=(10, 3),
        xlabel="",
        ylabel="",
        ylabel_lower="",
    )

    chart_image = ImageTk.PhotoImage(Image.open("chart.png"))

    chart = canvas.create_image(500, 305, image=chart_image)

    img0 = PhotoImage(file=f"img0.png")
    b0 = Button(
        image=img0,
        borderwidth=0,
        highlightthickness=0,
        command=update_ticker,
        relief="flat",
    )

    b0.place(x=926, y=85, width=121, height=41)

    entry0_img = PhotoImage(file=f"img_textBox0.png")
    entry0_bg = canvas.create_image(792.0, 105.5, image=entry0_img)

    entry0 = Entry(
        bd=0,
        highlightthickness=0,
        font=("Inter", int(20.0)),
        foreground="white",
        background="#1d2840",
    )

    entry0.bind("<Return>", update_ticker)  # type: ignore
    entry0.place(x=678, y=90, width=228.0, height=32)

    canvas.create_text(
        608.5,
        104.5,
        text="Ticker:",
        fill="#ffffff",
        font=("Inter SemiBold", int(24.0)),
    )

    price = canvas.create_text(
        410.0,
        107.5,
        text=format_to_brl(ticker["regularMarketPrice"]),
        fill="#ffffff",
        font=("Inter Bold", int(32.0)),
    )

    symbol = canvas.create_text(
        148.0,
        105.0,
        text=ticker["symbol"],
        fill="#ffffff",
        font=("Inter Bold", int(36.0)),
    )

    low_value = canvas.create_text(
        146.0,
        550.0,
        text=format_to_brl(ticker["fiftyTwoWeekLow"]),
        fill="#ffffff",
        font=("Inter SemiBold", int(30.0)),
    )

    high_value = canvas.create_text(
        410.0,
        550.0,
        text=format_to_brl(ticker["fiftyTwoWeekHigh"]),
        fill="#ffffff",
        font=("Inter SemiBold", int(30.0)),
    )

    volume = canvas.create_text(
        674.0,
        550.0,
        text=format_to_brl(ticker["averageDailyVolume3Month"]),
        fill="#ffffff",
        font=("Inter SemiBold", int(30.0)),
    )

    market_cap = canvas.create_text(
        938.0,
        550.0,
        text=format_to_brl(ticker["marketCap"]),
        fill="#ffffff",
        font=("Inter SemiBold", int(30.0)),
    )

    window.resizable(False, False)
    window.mainloop()


if __name__ == "__main__":
    main()
