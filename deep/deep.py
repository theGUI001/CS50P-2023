answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
answer = answer.strip().upper()

if answer in ["42", "FORTY TWO", "FORTY-TWO"]:
    print("Yes")
else:
    print("No")
