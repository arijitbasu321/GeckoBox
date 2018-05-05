def master_yoda(sentence):
    word_list = sentence.split()
    return " ".join(word_list[::-1])

user_input = input("Please enter a sentence ")

print(master_yoda(user_input))

