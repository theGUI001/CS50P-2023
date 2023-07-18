import re

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s: str) -> bool:

    valid_pattern = r'^[a-zA-Z]+([1-9]\d{1,5})?$'

    if len(s) < 2 or len(s) > 6:
        return False

    if re.match(valid_pattern, s):
        return True
    else:
        return False

main()