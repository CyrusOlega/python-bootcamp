guests = [
    "Mia Anderson",
    "Ethan Roberts",
    "Liam Johnson",
    "Sophia Martinez",
    "Olivia Davis",
    "Noah Thompson"
]
with open("test.txt", "w") as file:
    file.writelines([guest + "\n" for guest in guests])