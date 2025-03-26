# Opdracht 1 functies
# Naam student:
# Groep:


def volledige_naam(lijst_met_namen):
    """Genereer volledige namen uit een lijst met dictionaries"""
    for naam_dict in lijst_met_namen:
        # Verwijder lege tussenvoegsels en strip whitespace
        delen = [
            naam_dict["voornaam"],
            naam_dict["tussenvoegsel"],
            naam_dict["achternaam"]
        ]
        # Filter lege strings en join met spaties
        volledige_naam = " ".join(deel for deel in delen if deel.strip())
        print(volledige_naam)

# Voorbeeld gebruik:
if __name__ == "__main__":
    namen = [
        {"voornaam": "Willem", "tussenvoegsel": "van", "achternaam": "Dijk"},
        {"voornaam": "Klaas", "tussenvoegsel": "", "achternaam": "Wopstra"},
        {"voornaam": "Miep", "tussenvoegsel": "van der", "achternaam": "Plas"},
        {"voornaam": "Carla", "tussenvoegsel": "", "achternaam": "Hoogvliet"},
    ]
    volledige_naam(namen)