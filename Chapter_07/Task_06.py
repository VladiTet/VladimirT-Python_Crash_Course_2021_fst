prompt = "\nPlease enter your age for your ticket price: "
prompt += "\nType 'quit' to exit the program."

num = 1

while num <= 5:
    age = input(prompt)

    if age == 'quit':
        break

    age = int(age)

    if age > 0 and age <= 3:
        print("You are free!")
        num += 1
    elif age > 3 and age <= 13:
        print("You are $10.00")
        num += 1
    elif age > 13:
        print("You are $15.00")
        num += 1
    else:
        break
