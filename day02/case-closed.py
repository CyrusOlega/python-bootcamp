message = "I am perfectly calm and everything is fine"
lower_count = 0
upper_count = 0
space_count = 0

for character in message:
    if character.islower():
        lower_count += 1
    elif character.isupper():
        upper_count += 1
    elif character.isspace():
        space_count += 1

print(f"Lower case count: {lower_count}")
print(f"Upper case count: {upper_count}")
print(f"Space case count: {space_count}")