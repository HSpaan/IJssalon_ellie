from helper import decoreer

def print_aanbieding():
    prijzen = {
    "aardbei" : 3,
    "vanille" : 4,
    "chocolade" : 5
    }
<<<<<<< HEAD
=======

>>>>>>> a73349b7bf711e574816d2875d5448eadedef5b8
    aanbieding = (prijzen["aardbei"]) *0.8
    reclame_tekst = (f"Vandaag in de aanbieding: vanille-ijs, 1 liter - slechts {aanbieding}")
    reclame_tekst2 = (reclame_tekst[:61])
    reclame_tekst3 = (reclame_tekst2).upper()
    reclame_tekst4 = (reclame_tekst3).split()
    for el in reclame_tekst4:
        if len(el) < 5:
<<<<<<< HEAD
            print(el.lower())
        else:
            print(el.upper())

decoreer("aanbieding")
print_aanbieding()
=======
            print((el).lower())
        else:
            print((el).upper())

decoreer("Aanbieding")
print_aanbieding()
>>>>>>> a73349b7bf711e574816d2875d5448eadedef5b8
