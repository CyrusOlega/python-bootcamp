item_count = int(input("Enter number of items: "))
total = 0
for index, item in enumerate(range(item_count), start=1):
    item_price = int(input(f"Input item price #{index}: "))
    item_count = int(input(f"Input item count #{index}: "))
    total = item_price*item_count + total

print(f"Total Cost: {total}")