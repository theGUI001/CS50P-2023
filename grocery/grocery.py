grocery_list = {}

while True:
    try:
        item_input = input().upper()
    except EOFError:
        print()
        break
    else:
        pass

    if item_input in grocery_list:
        grocery_list[item_input] += 1
    else:
        grocery_list[item_input] = 1

grocery_list = dict(sorted(grocery_list.items()))

for key, value in grocery_list.items():
    print(f"{value} {key}")
