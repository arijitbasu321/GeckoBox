

def paper_doll(input_string):
    final_string  = ''
    for i,z in enumerate(input_string):
        final_string += input_string[i]*3

    return final_string

input_string = input("Enter a word: ")

print(paper_doll(input_string))
