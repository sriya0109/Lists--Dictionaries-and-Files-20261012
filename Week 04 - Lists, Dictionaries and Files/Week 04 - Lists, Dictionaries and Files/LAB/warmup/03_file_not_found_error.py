try:
    with open("records.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("records.txt not found")

