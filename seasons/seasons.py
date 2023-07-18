from datetime import date
import sys
import inflect


def main():
    birthday_date = input("Date of Birth: ")

    try:
        year, month, day = birthday_date.strip().split("-")

        year = int(year)
        month = int(month)
        day = int(day)
    except:
        sys.exit("Invalid Date")
    else:
        pass

    if not is_date_valid(year, month, day):
        sys.exit("Invalid Date")
    else:
        birthday_date = date(year, month, day)

    p = inflect.engine()

    minutes = p.number_to_words(age_in_minutes(birthday_date), andword="")

    print(f"{minutes.capitalize()} minutes")


def age_in_minutes(birthday: date) -> int:
    return (date.today() - birthday).days * 1440


def is_date_valid(yy: int, mm: int, dd: int) -> bool:
    if yy > date.today().year:
        return False

    if not 1 <= mm <= 12:
        return False

    if not 1 <= dd <= 31:
        return False

    try:
        _ = date(yy, mm, dd)
    except:
        return False
    else:
        return True


if __name__ == "__main__":
    main()
