def animal_crackers(text):
    text_list = text.lower().split()

    return text_list[0][0] == text_list[1][0]:


user_input = input("enter two words ")

result = animal_crackers(user_input)

if result:
    print("Both words start with the same alphabet.")
else:
    print("The words start with different alphabet.")
