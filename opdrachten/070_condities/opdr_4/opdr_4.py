# Opdracht 4 condities
# Naam student:
# Groep:


# Hier de rest van jouw code...

toppings = [("olijven", 4.50), ("kaas", 3.50), ("salami", 3.00), ("pepperoni", 2.00), ("ansjovis", 2.50)]

# Maak een lijst van alleen de topping namen voor de weergave
beschikbare_toppings = [topping[0] for topping in toppings]

# Vraag de gebruiker om een keuze
keuze = input(f"Maak een keuze uit onze toppings: {beschikbare_toppings}\n")

# Zoek de gekozen topping in de lijst
gevonden = False
for topping, prijs in toppings:
    if keuze.lower() == topping.lower():
        print(f"U heeft {topping} besteld. Dat kost {prijs}")
        gevonden = True
        break

if not gevonden:
    print("Uw keuze zit niet in ons assortiment")