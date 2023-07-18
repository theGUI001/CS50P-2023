import random


def main():
    score = 0
    level = get_level()

    for _ in range(0,10):
        n1 = generate_integer(level)
        n2 = generate_integer(level)
        correct_answer = n1 + n2
        for i in range(3):
            try:
                answer = int(input(f"{n1} + {n2} = "))
            except ValueError:
                answer = ''
            if answer == correct_answer:
                score += 1
                break
            else:
                print("EEE")
                if i == 2:
                    print(f"{n1} + {n2} = {correct_answer}")

    print(f"Score: {score}")


def get_level() -> int:
    while True:
        try:
            level = int(input("Level : "))
        except ValueError:
            pass
        else:
            if 1 <= level <= 3:
                return level


def generate_integer(level: int) -> int:
    if 1 <= level <= 3:
        match level:
            case 1:
                number = random.randint(0, 9)
            case 2:
                number = random.randint(10, 99)
            case 3:
                number = random.randint(100, 999)
        return number
    else:
        raise ValueError


if __name__ == "__main__":
    main()
