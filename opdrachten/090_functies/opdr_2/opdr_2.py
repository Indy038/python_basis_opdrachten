# Opdracht 1 functies
# Naam student:
# Groep:


def kilometers_naar_miles(km):
    """Converteer kilometers naar miles"""
    return km / 1.609344

def miles_naar_kilometers(miles):
    """Converteer miles naar kilometers"""
    return miles * 1.609344

# Voorbeeld gebruik:
if __name__ == "__main__":
    kilometers = 1223
    miles = 867
    
    # Conversies uitvoeren
    miles_resultaat = kilometers_naar_miles(kilometers)
    km_resultaat = miles_naar_kilometers(miles)
    
    # Resultaten printen
    print(f"{kilometers} kilometers = {miles_resultaat} miles")
    print(f"{miles} miles = {km_resultaat} kilometers")