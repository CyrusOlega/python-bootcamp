def line_generator(line_count, message):
    for item in range(line_count):
        print(f"{message} {item}")

line_generator(line_count=3, message="Hello World")