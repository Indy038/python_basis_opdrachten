# Opdracht 2 tekstbestanden
# Naam student:
# Groep:


# De rest moet jij doen.....

import random

def raad_het_getal():
    geheim_getal = random.randint(1, 100)
    aantal_pogingen = 0
    
    print("Raad mijn geheime getal tussen 1 en 100")
    
    while True:
        try:
            gok = int(input())
            aantal_pogingen += 1
            
            if gok < geheim