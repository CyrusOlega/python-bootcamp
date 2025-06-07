attendee_names = set()
attendee_count = int(input("How many attendees? "))

for count in range(attendee_count):
    attendee_names.add(input("Attendee name: "))

print("Attendees:", end=" ")
print(*attendee_names, sep=", ")
