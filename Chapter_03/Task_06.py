guests = ['❤Nikol❤', 'Viktoria', 'Monika', 'Kristina']

for x in guests:
    print(f"{x}, please come to dinner.")

name = guests[1].title()
print(f"\nSorry, {name} can't come to the dinner.\n")

del(guests[1])
guests.insert(1, 'Magi')

for x in guests:
    print(f"{x}, please come to dinner.")

print("\nWe got a bigger table!\n")
guests.insert(0, 'Bobi')
guests.insert(int(len(guests)/2), 'Tisho')
guests.append('Aleksander')

for x in guests:
    print(f"{x}, please come to dinner.")
