# Opdracht 3 input functie
# Naam student:
# Groep:

# Hier komt je code...

# Hier start de for-loop

pizzas = ['margharita', 'calzone', 'verdi', 'olivio', 'quattro stagioni']
pizzas.sort()  # Sorteer op alfabet
pizzas.append('yo-favorito')  # Voeg pizza toe
pizzas.remove('olivio')  # Verwijder minst favoriet
print(pizzas[:3])  # Eerste 3
print([pizzas[len(pizzas)//2]])  # Middelste (werkt voor oneven lengtes)
print(pizzas[-3:])  # Laatste 3