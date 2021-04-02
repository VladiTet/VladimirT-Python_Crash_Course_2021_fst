# Make an empty list to store people in.
people = []

# Define some people, and add them to the list.
person = {
    'first_name': 'George',
    'last_name': 'Ivanov',
    'age': 25,
    'city': 'Sofia',
    }
people.append(person)

person = {
    'first_name': 'Jack',
    'last_name': 'Tylor',
    'age': 30,
    'city': 'Sliven',
    }
people.append(person)

person = {
    'first_name': 'Boris',
    'last_name': 'Borisov',
    'age': 18,
    'city': 'Stara Zagora',
    }
people.append(person)

# Display all of the information in the dictionary.
for person in people:
    name = f"{person['first_name'].title()} {person['last_name'].title()}"
    age = person['age']
    city = person['city'].title()
    
    print(f"{name}, of {city}, is {age} years old.")
