# Opdracht 2 berekeningen
# Naam student:
# Groep:

# Hier komt je code...

gasten = ["Indy", "Paul", "Kees", "Marie", "Hilda"]
print("Beginnende gastenlijst:", gasten)


gasten.remove("Marie")
print("Na het verwijderen van Marie:", gasten)


index_kees = gasten.index("Kees")  # Vind de index van Kees
gasten.insert(index_kees + 1, "George")  # Voeg George direct na Kees toe
print("Na het toevoegen van George:", gasten)
