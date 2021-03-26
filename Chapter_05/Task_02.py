car = 'subaru'

print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

#checking for Equality
print("\nhecking for Equality")

car = 'bmw'
print(car == 'bmw')

car = 'audi'
print(car == 'bmw')

#ignoring case when Checking for equality
print("\nignoring case when Checking for equality")

car = 'Audi'
print(car == 'audi')

car = 'Audi'
print(car.lower() == 'audi')

#checking for inequality
print("\nchecking for inequality")

requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("Hold the anchovies!")

#numerical comparisons
print("\nnumerical comparisons")

age = 18
print(age == 18)
age = 19
print(age < 21)
print(age <= 21)
print(age > 21)
print(age >= 21)

answer = 17

if answer != 42:
    print("That is not the correct answer. Please try again!")

age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)

age_1 = 22
print(age_0 >= 21 and age_1 >= 21)

age_0 = 22
age_1 = 18
print(age_0 >= 21 or age_1 >= 21)

age_0 = 18
print(age_0 >= 21 or age_1 >= 21)

#value is in a list
print("\nvalue is in a list")

requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings)
print('pepperoni' in requested_toppings)


#value is not in a list
print("\nvalue is not in a list")

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")

