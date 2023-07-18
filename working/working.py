import re


def main():
    print(convert(input("Hours: ")))


def convert(s: str) -> str:
    if not re.match(r"^\d{1,2}(:\d{2})? [AP]M to \d{1,2}(:\d{2})? [AP]M$", s):
        raise ValueError("Invalid input format")

    start, end = s.split(" to ")

    start_time, start_meridiem = start.split(" ")
    end_time, end_meridiem = end.split(" ")

    if ":" in start_time:
        start_hour, start_minute = map(int, start_time.split(":"))
    else:
        start_hour, start_minute = int(start_time), 0

    if ":" in end_time:
        end_hour, end_minute = map(int, end_time.split(":"))
    else:
        end_hour, end_minute = int(end_time), 0

    if (
        not (0 <= start_hour <= 12)
        or not (0 <= end_hour <= 12)
        or not (0 <= start_minute < 60)
        or not (0 <= end_minute < 60)
    ):
        raise ValueError("Invalid time")

    if start_meridiem == "PM" and start_hour != 12:
        start_hour += 12
    elif start_meridiem == "AM" and start_hour == 12:
        start_hour = 0

    if end_meridiem == "PM" and end_hour != 12:
        end_hour += 12
    elif end_meridiem == "AM" and end_hour == 12:
        end_hour = 0

    return f"{start_hour:02}:{start_minute:02} to {end_hour:02}:{end_minute:02}"


if __name__ == "__main__":
    main()
