greeting = input("Greeting: ").strip().lower()

if greeting.__contains__("hello"):
    print("$0")
elif greeting[0] == "h":
    print("$20")
else:
    print("$100")