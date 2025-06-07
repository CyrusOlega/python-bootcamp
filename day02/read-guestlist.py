with open("test.txt", "r") as file:
    guests = file.read().splitlines()
    print(guests)