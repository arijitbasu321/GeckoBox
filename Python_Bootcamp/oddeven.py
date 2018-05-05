

def less_of_two_evens(num1,num2):
    if num1 % 2 == 0 and num2 % 2 == 0:
        if num1 > num2:
            print(num1)
        else:
            print(num2)
    else:
        if num1 > num2:
            print(num1)
        else:
            print(num2)

user_input = list(map(int, input("enter two numbers: ").split()))

num1 = user_input[0]
num2 = user_input[1]

less_of_two_evens(num1, num2)


