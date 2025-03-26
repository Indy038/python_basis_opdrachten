# Opdracht 1 functies
# Naam student:
# Groep:


def write_to_file(bestandsnaam, tekst):
    """Schrijft tekst naar een bestand, voegt toe als bestand al bestaat"""
    try:
        with open(bestandsnaam, 'a') as bestand:  # 'a' mode voor append
            bestand.write(tekst + '\n')  # Voeg nieuwe regel toe
        print(f"Tekst succesvol geschreven naar {bestandsnaam}")
    except Exception as e:
        print(f"Fout bij schrijven naar bestand: {e}")

# Voorbeeld gebruik:
if __name__ == "__main__":
    my_tekst = "Schrijf dit maar even in een bestandje"
    my_file = "test.txt"
    write_to_file(my_file, my_tekst)
