favorite_pizzas = ['pepperoni', 'kaprichoza', 'kalcone']
friend_pizzas = favorite_pizzas[:]

favorite_pizzas.append("meat lover's")
friend_pizzas.append('pesto')

print("My favorite pizzas are:")
for x in favorite_pizzas:
    print(f"-{x}")

print("\nMy friend’s favorite pizzas are:")
for x in friend_pizzas:
    print(f"-{x}")



