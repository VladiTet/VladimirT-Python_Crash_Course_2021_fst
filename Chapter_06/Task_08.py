pets = []

pet = {
    'animal type': 'python',
    'name': 'John',
    'owner': 'Petar',
    'weight': 43,
    'eats': 'bugs',
}
pets.append(pet)

pet = {
    'animal type': 'chicken',
    'name': 'Tobi',
    'owner': 'Ivailo',
    'weight': 2,
    'eats': 'seeds',
}
pets.append(pet)

pet = {
    'animal type': 'dog',
    'name': 'Rex',
    'owner': 'Hristo',
    'weight': 37,
    'eats': 'shoes',
}
pets.append(pet)


for pet in pets:
    print(f"\nHere's what I know about {pet['name'].title()}:")
    for key, value in pet.items():
        print(f"\t{key}: {value}")

