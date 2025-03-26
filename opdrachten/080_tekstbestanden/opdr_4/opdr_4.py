# Opdracht 4 Tekst opslaan
# Naam student:
# Groep:


# Party enquete

def verzamel_gegevens():
    vragen = [
        "Wat is je voornaam?",
        "Wat is je achternaam?",
        "Wat neem je mee aan drank?",
        "Wat neem je mee om te eten?"
    ]
    
    antwoorden = {}
    
    print("Vul alstublieft de vragenlijst in voor de party:")
    for i, vraag in enumerate(vragen, start=1):
        antwoord = input(f"{i}. {vragen[i-1]}\n")
        sleutel = ["voornaam", "achternaam", "drank", "eten"][i-1]
        antwoorden[sleutel] = antwoord
    
    print("\nBedankt voor het invullen!")
    print("See you at the party.\n")
    return antwoorden

def schrijf_naar_bestand(gegevens, bestandsnaam="party_gasten.txt"):
    with open(bestandsnaam, "a") as bestand:
        bestand.write("----\n")
        for sleutel, waarde in gegevens.items():
            bestand.write(f"{sleutel}: {waarde}\n")
        bestand.write("\n")

if __name__ == "__main__":
    while True:
        gast = verzamel_gegevens()
        schrijf_naar_bestand(gast)
        
        doorgaan = input("Wil je nog een gast toevoegen? (ja/nee)\n").lower()
        if doorgaan != 'ja':
            break