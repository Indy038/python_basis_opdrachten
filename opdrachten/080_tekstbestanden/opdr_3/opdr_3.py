# Opdracht 3 Tekst opslaan
# Naam student:
# Groep:

def caesar_encrypt(tekst, verschuiving=5):
    resultaat = ""
    for karakter in tekst:
        if karakter.isalpha():
            # Bepaal basis voor hoofdletters of kleine letters
            basis = ord('A') if karakter.isupper() else ord('a')
            # Verschuif het karakter
            nieuwe_code = (ord(karakter) - basis + verschuiving) % 26 + basis
            resultaat += chr(nieuwe_code)
        else:
            # Behoud niet-alfabetische karakters
            resultaat += karakter
    return resultaat

# Vraag om invoer van de gebruiker
tekst = input("Geef de tekst die je wilt encrypten..\n")

# Versleutel de tekst
versleutelde_tekst = caesar_encrypt(tekst)

# Toon het resultaat
print(versleutelde_tekst)

