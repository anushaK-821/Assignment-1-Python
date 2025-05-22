def character_counter(input):
    char_count = {}

    for char in input:
        if char != ' ': 
            char = char.lower()
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

    return char_count

input = input("Enter a string: ")
print(character_counter(input))
