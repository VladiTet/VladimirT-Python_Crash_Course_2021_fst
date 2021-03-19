guests = ['❤Nikol❤', 'Viktoria', 'Monika', 'Kristina']

for x in guests:
    print(f"{x}, please come to dinner.")
print(len(guests))

name = guests[1].title()
print(f"\nSorry, {name} can't come to the dinner.\n")

del(guests[1])
guests.insert(1, 'Magi')

for x in guests:
    print(f"{x}, please come to dinner.")

print("\nWe got a bigger table!\n")
guests.insert(0, 'Bobi')
guests.insert(2, 'Tisho')
guests.append('Aleksander')

for x in guests:
    print(f"{x}, please come to dinner.")

print(len(guests))

print("\nSorry, we can only invite two people to dinner.\n")

for x in range(0,5):
    name = guests.pop()
    print(f"Sorry, {name.title()} there's no room at the table.")

print('\n')

for x in guests:
    print(f"{x}, please come to dinner.")

print(len(guests))

del(guests[0])
del(guests[0])

print(guests)
