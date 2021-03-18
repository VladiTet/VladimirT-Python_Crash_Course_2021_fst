guests = ['❤Nikol❤', 'Viktoria', 'Monika', 'Kristina']

for x in guests:
    print(f"{x}, please come to dinner.")

name = guests[1].title()
print(f"\nSorry, {name} can't come to the dinner.\n")

del(guests[1])
guests.insert(1, 'Magi')

for x in guests:
    print(f"{x}, please come to dinner.")
