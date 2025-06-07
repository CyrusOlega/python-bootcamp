attendee_names = []
attendee_count = int(input("How many attendees? "))

for count in range(attendee_count):
    attendee_names.append(input(f"Attendee Name: "))

print(*attendee_names, sep=", ")
print(f"Same Name: {attendee_names.count("Cyrus")}")