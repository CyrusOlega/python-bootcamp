class LockedDoor:
    def __init__(self, closed):
        self.closed = closed
        self.locked = False

    def open(self):
        if self.closed:
            self.closed = False
            print("The door has been opened")
        elif self.locked:
            print("The door is locked")
        else:
            print("The door is already open")

    def close(self):
        if self.closed:
            print("The door is already closed")
        else:
            print("The door has been closed")
            self.closed = True

    def lock(self):
        if self.locked:
            print("The door is already locked")
        elif not self.closed:
            print("Cannot lock door when it is open")
        else:
            print("The door has been locked")
            self.locked = True

    def unlock(self):
        if not self.locked or not self.closed:
            print("The door is already unlocked")
        else:
            self.locked = False
            print("The door has been unlocked")

locked_door = LockedDoor(True)
locked_door.open()
print(f"Closed: {locked_door.closed}")
print(f"Locked: {locked_door.locked}")

locked_door.close()
print(f"Closed: {locked_door.closed}")
print(f"Locked: {locked_door.locked}")

locked_door.unlock()
print(f"Closed: {locked_door.closed}")
print(f"Locked: {locked_door.locked}")

locked_door.open()
locked_door.lock()
print(f"Closed: {locked_door.closed}")
print(f"Locked: {locked_door.locked}")

locked_door.close()
locked_door.lock()
print(f"Closed: {locked_door.closed}")
print(f"Locked: {locked_door.locked}")
