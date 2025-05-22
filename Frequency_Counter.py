def word_frequency(paragraph):
    words = paragraph.lower().split() 
    freq = {}

    for word in words:
        word = word.strip('.,!?;:"()') 
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1

    return freq

paragraph = input("Enter the paragraph : ")
print(word_frequency(paragraph))
