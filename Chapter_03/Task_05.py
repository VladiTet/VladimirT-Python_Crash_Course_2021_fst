guests = ['❤Nikol❤', 'Viktoria', 'Monika', 'Kristina']

for x in guests:
    print(f"{x}, please come to dinner.")

del(guests[1])
guests.insert(1, 'Magi')

for x in guests:
    print(f"{x}, please come to dinner.")
