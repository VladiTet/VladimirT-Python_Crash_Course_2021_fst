favorite_numbers = {
    'Maria': [8, 12],
    'Nikol': [26, 6],
    'George': [5, 55],
    'Aleksander': [14, 28], 
    'Dimitar': [16, 21, 36],
    }

for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()} likes the following numbers:")
    for number in numbers:
        print(f"  {number}")
