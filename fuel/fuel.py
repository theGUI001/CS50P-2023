from typing import List

def main():
    while True:
        x, y = get_fraction("Fraction: ")

        try:
            percentage = round(x / y * 100)
        except ZeroDivisionError:
            pass
        else:
            if percentage <= 100:
                break

    if percentage >= 99:
        print("F")
    elif percentage <= 1:
        print("E")
    else:
        print(f"{percentage}%")


def get_fraction(prompt:str) -> List[int]:
    while True:
        usr_input = input(prompt).split("/")
        try:
            return int(usr_input[0]), int(usr_input[1])
        except ValueError:
            pass


if __name__ == "__main__":
    main()