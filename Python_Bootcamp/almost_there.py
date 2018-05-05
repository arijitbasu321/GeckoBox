def almost_there(n):
    if 90  <= n <= 110 or 190 <= n <= 210:
        return  True
    else:
        return False

user_input = int(input("Enter a number ").strip())

print(almost_there(user_input))
