# Opdracht 1 while-loops
# Naam student:
# Groep:

# Jouw code komt hier

# Enquête vragen
vragen = [
    "Wat vind je van de huidige regering?",
    "Wat vind je van de Python-lessen tot nu toe?",
    "Wat vind jij de mooiste stad van Nederland?"
]

# Antwoorden verzamelen
antwoorden = []
print("Beantwoord alstublieft de volgende vragen:")
for vraag in vragen:
    antwoord = input(vraag + "\n")
    antwoorden.append(antwoord)

# Resultaten opslaan in een tekstbestand
with open("enquete_resultaten.txt", "w") as bestand:
    bestand.write("=== Enquête Resultaten ===\n\n")
    for i in range(len(vragen)):
        bestand.write(f"Vraag {i+1}: {vragen[i]}\n")
        bestand