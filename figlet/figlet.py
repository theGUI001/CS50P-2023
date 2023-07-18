from pyfiglet import Figlet
import sys
from random import choice

figlet = Figlet()

valid_fonts = figlet.getFonts()

argc = len(sys.argv)

# print(argc)

if argc == 1 or argc == 3:
    if argc == 1:
        text = input("Input: ")
        print("Output: ")
        figlet.setFont(font=choice(valid_fonts))
        print(figlet.renderText(text))
    elif sys.argv[1] in ["-f", "--font"] and sys.argv[2] in valid_fonts:
        text = input("Input: ")
        print("Output: ")
        figlet.setFont(font=sys.argv[2])
        print(figlet.renderText(text))
    else:
        sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")
