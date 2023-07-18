import sys
from PIL import Image, ImageOps

argc = len(sys.argv)

if argc > 3:
    sys.exit("Too many command-line arguments")
elif argc < 3:
    sys.exit("Too few command-line arguments")

if not sys.argv[1][-3:] == sys.argv[2][-3:]:
    sys.exit("Input and output have different extensions")

shirt = Image.open("shirt.png")
try:
    before = Image.open(sys.argv[1])
except FileNotFoundError:
    sys.exit("Input does not exists")
else:
    pass

before = ImageOps.fit(before, shirt.size)

before.paste(shirt, shirt)

before.save(sys.argv[2])

shirt.close()
before.close()
