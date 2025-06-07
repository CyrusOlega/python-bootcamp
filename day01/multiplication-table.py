invalid = True

while invalid:
    try:
        number = int(input("Pick a number: "))
        invalid = False

        for item in range(1, 11):
            print(f"{number} x {item} = {number * item}")
    except ValueError:
        print("Input is not a number")