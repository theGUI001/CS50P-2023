text_input = input("Input: ")
vowels = ["a","e","i","o","u","A","E","I","O","U"]

print("Output: ", end="")

for letter in text_input:
    if letter in vowels:
        pass
    else:
        print(letter, end="")

print()