# Opdracht 3 input functie
# Naam student:
# Groep:

# Hier komt je code...

# Hier start de for-loop

# Maak een lege lijst om de resultaten op te slaan
resultaten = []

# Loop van 3 tot 81 met stappen van 3
for i in range(3, 82, 3):  
    resultaat = (i ** 2) / 3  # Kwadraat van het getal nemen en delen door 3
    resultaten.append(resultaat)  # Toevoegen aan de lijst

# Print de lijst met de resultaten
print(resultaten)
