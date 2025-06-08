class Pen:
    def __init__(self, brand, color, capped, ink_level):
        self.brand = brand
        self.color = color
        self.capped = capped
        self.ink_level = ink_level

    def cap(self):
        self.capped = True

    def uncap(self):
        self.capped = False

    def write(self, paper, text):
        paper.contents = text
        self.ink_level -= 10

    def refill(self, amount):
        if amount < 0:
            print("Cannot use negative amounts")
        else:
            self.ink_level += amount

class Paper:
    def __init__(self, contents=""):
            self.contents = contents

pilot = Pen("Pilot", "Black", True, 100)
paper = Paper()
print(f"Pilot is capped: {pilot.capped}")
pilot.uncap()
print(f"Pilot is capped: {pilot.capped}")

print(f"Ink Level: {pilot.ink_level}")

print(f"Paper contents: {paper.contents}")
pilot.write(paper, "Hello World")
print(f"Paper contents: {paper.contents}")

print(f"Ink Level: {pilot.ink_level}")
pilot.refill(10)
print(f"Ink Level: {pilot.ink_level}")
