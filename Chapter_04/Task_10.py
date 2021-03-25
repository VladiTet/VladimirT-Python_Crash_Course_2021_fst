players = ['charles', 'martina', 'michael', 'florence', 'eli']

print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

print("\nHere are the three players from middle on my team:")
for player in players[1:4]:
    print(player.title())

print("\nHere are the last three players on my team:")
for player in players[-3:]:
    print(player.title())
