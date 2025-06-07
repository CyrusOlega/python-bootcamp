attendees = dict()
attendee_count = int(input("How many attendees? "))

for count in range(attendee_count):
    name = input("Attendee name: ")
    task = input("Attendee task: ")
    attendees[name] = task

print(attendees)