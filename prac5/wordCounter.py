string = input("Text: ")
dictionary = {}
max_word_length = 0
for word in string.split():
    if len(word) > max_word_length:
        max_word_length = len(word)
    if word.lower() in dictionary:
        dictionary[word.lower()] += 1
    else:
        dictionary[word.lower()] = 1

sorted(dictionary)

for word in dictionary:
    print("{:{}}: {}".format(word, max_word_length + 1, dictionary[word]))

