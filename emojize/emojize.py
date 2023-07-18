import emoji

usr_input = input("Input: ")

if usr_input.__contains__("_"):
    output = emoji.emojize(usr_input)
else:
    output = emoji.emojize(usr_input, language="alias")

print(f"Output: {output}")
