# Opdracht 3 input functie
# Naam student:
# Groep:

# Hier komt je code...

input_waarden = input("Zwolle, Haarlem, Zaandam, Amsterdam, Roermond")

# Zet de invoer om in een lijst en verwijder eventuele spaties rondom de woorden
objecten = [item.strip() for item in input_waarden.split(",")]

# Controleer of er minimaal 5 objecten zijn
if len(objecten) < 5:
    print("Zwolle, Haarlem, Zaandam, Amsterdam, Roermond")
    objecten.sort(reverse=True)
    