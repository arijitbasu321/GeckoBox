

def summer_of_69(input_list):
    index_of_6 = input_list.index(6)
    index_of_9 = input_list.index(9)

    output_list = input_list[:index_of_6] + input_list[index_of_9 + 1:]
    return sum(output_list)

input_list = list(map(int, input("Enter list of numbers ").split()))

print(summer_of_69(input_list))

