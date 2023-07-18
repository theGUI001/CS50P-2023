n1, operation, n2 = input("Expression: ").strip().split(" ")

n1 = float(n1)
n2 = float(n2)

match operation:
    case "+":
        print(f"{(n1+n2):.1f}")
    case "-":
        print(f"{(n1-n2):.1f}")
    case "*":
        print(f"{(n1*n2):.1f}")
    case "/":
        print(f"{(n1/n2):.1f}")
