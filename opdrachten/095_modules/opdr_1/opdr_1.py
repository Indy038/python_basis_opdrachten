# Opdracht 1 functies
# Naam student: Kevin Bonestroo
# Groep: IT2A

# importeer de module csv...
from my_modules import csv_module as csv

def main():
    data = csv.lees_csv('voorbeeld.csv')
    for rij in data:
        print(rij)

if __name__ == "__main__":
    main()