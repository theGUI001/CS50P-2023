def main():
    greeting = input("Greeting: ")
    print(f"${value(greeting)}")


def value(greeting: str) -> int:
    if type(greeting) is not str:
        raise TypeError
    else:
        greeting = greeting.strip().lower()
        if greeting.__contains__("hello"):
            return 0
        elif len(greeting) > 0 and greeting[0] == "h":
            return 20
        else:
            return 100


if __name__ == "__main__":
    main()
