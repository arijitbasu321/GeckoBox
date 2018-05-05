def old_macdonald(text):
    text = text.capitalize()
    return text[:3] + text[3].upper() + text[4:]


user_input = input("enter you name: ")

print(old_macdonald(user_input))
