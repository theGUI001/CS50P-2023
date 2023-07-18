varName = input("camelCase: ")

print("snake_case: ", end="")

for letter in varName:
    if letter.isupper():
        print(f"_{letter.lower()}",end="")
    else:
        print(letter,end="")
print()
