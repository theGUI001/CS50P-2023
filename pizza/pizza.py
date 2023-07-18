import sys
import csv
from tabulate import tabulate

argc = len(sys.argv)

if argc > 2:
    sys.exit("Too many command-line arguments")
elif argc < 2:
    sys.exit("Too few command-line arguments")

if not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")

try:
    with open(sys.argv[1]) as file:
        reader = csv.reader(file)
        print(tabulate(reader, headers="firstrow", tablefmt="grid"))
except FileNotFoundError:
    sys.exit("File does not exist")
