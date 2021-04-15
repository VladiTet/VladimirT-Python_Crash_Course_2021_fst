players = ['charles', 'martina', 'michael', 'florence', 'eli', 'martin',
           'George']

print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

print("\nHere are the three players from middle on my team:")
for player in players[int(len(players)/2 - 1):int(len(players)/2) + 2]:
    print(player.title())

print("\nHere are the last three players on my team:")
for player in players[-3:]:
    print(player.title())
