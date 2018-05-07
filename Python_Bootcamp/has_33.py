

def has_33(input_list):
    for i,j in enumerate(input_list):
        if input_list[i] == 3 and i < len(input_list) - 1:
            if input_list[i+1] == 3:
                x = 33
                break
            else:
                continue
        else:
            x = 0
    return True if x == 33 else False

input_list = list(map(int, input("Enter list of numbers: ").split()))

print(has_33(input_list))
