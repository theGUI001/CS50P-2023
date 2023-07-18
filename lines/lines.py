import sys

argc = len(sys.argv)

if argc > 2:
    sys.exit("Too many command-line arguments")
elif argc < 2:
    sys.exit("Too few command-line arguments")

if not sys.argv[1].endswith(".py"):
    sys.exit("Not a Python file")

lines_counter = 0

try:
    with open(sys.argv[1]) as file:
        for line in file:
            if line.lstrip().startswith("# ") or len(line.strip()) == 0:
                pass
            else:
                lines_counter += 1
except FileNotFoundError:
    sys.exit("File does not exist")

print(lines_counter)
