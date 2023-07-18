calories = {"apple": 130,
            "avocado" : 50,
            "banana": 110,
            "grapefruit" : 60,
            "grapes" : 90,
            "kiwifruit" : 90,
            "lemon": 15,
            "orange" : 80,
            "peach" : 60,
            "pear" : 100,
            "pineapple" : 50,
            "strawberries" : 50,
            "tangerine" : 50,
            "watermelon" : 80,
            "sweet cherries" : 100
            }

fruit = input("Item: ")
fruit = fruit.lower()

if fruit in calories:
    print(f"Calories: {calories[fruit]}")
