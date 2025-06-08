class Door:
    def __init__(self, closed):
        self.closed = closed

    def open(self):
        if self.closed:
            self.closed = False
        else:
            print("The door is already open")

    def close(self):
        if self.closed:
            print("The door is already closed")
        else:
            self.closed = True

door = Door(closed=True)
door.open()
door.open()
