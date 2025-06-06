count = 0
stop_program = False
while not stop_program:
    choice = input("Provide command: ")
    match choice:
        case "add":
            count += 1
            print(f"Count is now {count}")
        case "minus":
            count -= 1
            print(f"Count is now {count}")
        case "exit":
            stop_program = True