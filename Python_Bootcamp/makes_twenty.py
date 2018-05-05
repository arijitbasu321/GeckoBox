
def makes_twenty(num1, num2):
    if num1 + num2 == 20:
        return True
    elif num1 == 20 or num2 == 20:
        return True
    else:
        return False

user_input = list(map(int, input("Enter two numbers ").split()))
num1 = user_input[0]
num2 = user_input[1]
print(makes_twenty(num1, num2))
