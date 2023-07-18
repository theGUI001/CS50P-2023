def main():
    text_input = input("Input: ")
    print("Output: ", end="")
    print(shorten(text_input))


def shorten(word: str) -> str:
    if type(word) is not str:
        raise TypeError
    else:
        vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        for vowel in vowels:
            word = word.replace(vowel, "")
        return word


if __name__ == "__main__":
    main()
