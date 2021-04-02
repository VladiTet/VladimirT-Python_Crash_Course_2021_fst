favorite_places = {

    'Tino': ['mountain', 'ice cream', 'spontaneity'],
    'Velizar': ['Hawaii', 'iceland'],
    'Magi': ['flowers', 'walks', 'Las Vegas']
    
    }

for name, places in favorite_places.items():
    print(f"\n{name.title()} likes the following places:")
    for place in places:
        print(f"- {place.title()}")

