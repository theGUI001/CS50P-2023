import sys
import csv

argc = len(sys.argv)

if argc > 3:
    sys.exit("Too many command-line arguments")
elif argc < 3:
    sys.exit("Too few command-line arguments")

if not sys.argv[1].endswith(".csv"):
    sys.exit(f"Could not read {sys.argv[1]}")

old_csv = open(sys.argv[1])
new_csv = open(sys.argv[2], "w")

try:
    old_file = csv.DictReader(old_csv)
except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")

new_file_readers = ["first", "last", "house"]
new_file = csv.DictWriter(new_csv, fieldnames=new_file_readers)

new_file.writeheader()

for row in old_file:
    last, first = row["name"].split(", ")
    new_file.writerow({"first": first, "last": last, "house": row["house"]})

old_csv.close()
new_csv.close()
