def count_vowels(string:str) -> int:
    vowels = "aeiou"
    count = 0
    for char in string:
        if char.lower() in vowels:
            count += 1

    return count

print(count_vowels("Python Training Course"))