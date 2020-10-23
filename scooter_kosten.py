def bereken_maandkosten(km_per_maand):
    verzekering_per_maand = 23
    benzine_kosten_per_liter = 1.54
    liter_per_kilometer = 0.2


    maandkosten = int(km_per_maand * liter_per_kilometer * benzine_kosten_per_liter) + verzekering_per_maand
    return maandkosten



invoer = ""

# Zolang de invoer geen float is, wordt deze while loop uitgevoerd
while not isinstance(invoer, float):

    # probeer of deze code werkt
    try:
        #Vraag om een getal en sla op in de variabele: invoer
        invoer = input("Hoeveel kilometer rij je per maand? ")

        # Probeer de input om te zetten in een float (getal met cijfers achter de komma)
        invoer = float(invoer)
        
        kosten = bereken_maandkosten(invoer)
        
        print("de kosten van je scooter zijn €"  + str(kosten))

    except ValueError:
        # Als er een ValueError optreedt, dan voer je deze code uit
        print(invoer + " is geen geldig getal!")

        

  


  
