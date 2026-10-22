from algemene_functies import mijn_functie_2

def aanbieding_1(smaak, prijs, korting):
    korting_prijs = prijs - prijs * korting

    return smaak, korting_prijs

lekker, korting_prijs = aanbieding_1("aardbei", 4, 0.1)

print(f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {lekker}, van 4 euro voor {korting_prijs:.2f} euro.")


def inkomsten_totaal(inkomsten, BTW):
    optelling = 0
    
    for i in inkomsten:
        optelling += i

    belasting = optelling * BTW

    return optelling, belasting

totaal, bel = inkomsten_totaal([220, 430, 125, 160, 205, 90, 345], 0.09)

print(f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {bel} euro btw betaald dient te worden.")


def laag_en_hoog(mijn_lijst):
  hoogste = max(mijn_lijst)
  laagste = min(mijn_lijst)
  return [hoogste, laagste]

h, l = laag_en_hoog([220, 430, 125, 205, 90, 345])

print(h, l)


def gemiddelde(mijn_lijst):
  aantal = len(mijn_lijst)
  totaal = sum(mijn_lijst)
  return aantal, totaal

a, t = gemiddelde([220, 430, 125, 205, 90, 345])

g = t / a

print(f"De gemiddelde inkomsten deze week zijn {g:.2f} euro.")

