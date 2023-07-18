def main():
    fraction = input("Fraction: ").strip()
    percentage = convert(fraction)
    print(gauge(percentage))


def convert(fraction: str) -> int:
    if type(fraction) is not str:
        raise TypeError
    else:
        pass

    if fraction.__contains__("/"):
        x, y = fraction.split("/")

        x = int(x)
        y = int(y)

        if y == 0:
            raise ZeroDivisionError

        if type(x) is not int or type(y) is not int or x > y:
            raise ValueError

    else:
        raise ValueError

    return round(x / y * 100)


def gauge(percentage: int) -> str:
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
