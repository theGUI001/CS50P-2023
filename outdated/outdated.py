months_names = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]


def main():
    while True:
        input_date = input("Date: ").strip()

        try:
            month, day, year = input_date.split("/")
            if is_date_valid(int(month), int(day)):
                break

        except ValueError:
            try:
                month, day, year = input_date.split(" ")
                if day.__contains__(","):
                    day = day.replace(",", "")
                    year = year.strip()

                    if month in months_names:
                        month = months_names.index(month) + 1

                    if is_date_valid(month, int(day)):
                        break
            except ValueError:
                pass

    print(f"{year}-{int(month):02d}-{int(day):02d}")


def is_date_valid(mm: int, dd: int) -> bool:
    if 1 <= mm <= 12 and 1 <= dd <= 31:
        return True

    return False


if __name__ == "__main__":
    main()
