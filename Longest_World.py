def find_longest_word(sentence):
    words = sentence.split()
    longest = max(words, key=len)
    return longest

user_input = input("Enter a sentence: ")
longest = find_longest_word(user_input)

print("The longest word is:", longest)
