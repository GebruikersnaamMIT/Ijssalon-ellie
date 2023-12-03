from algemene_functies import mijn_functie_2 

def aanbieding_1(smaak, prijs, korting):
    actie_prijs = prijs - ((prijs/korting)/ 100)
    actie_prijs = "{:.2f}".format(actie_prijs)
    return print(f"Vaandaag in de aanbieding: emmertje ijs (1 litel) in de smaak van {smaak}, van {prijs} euro voor {actie_prijs} euro.")

def inkomsten_totaal(inkomsten, btw):
    length = len(inkomsten)
    totaal = 0
    for i in range(length):
        totaal += inkomsten[i]
        
    bedrag = totaal * btw / 100
    return print(f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {bedrag} euro btw betaald dient te worden.")

def laag_en_hoog(mijn_lijst):
    result = []
    result.append(min(mijn_lijst))
    result.append(max(mijn_lijst))
    return result

def gemiddelde(mijn_lijst):
    gemiddelde = sum(mijn_lijst) / len(mijn_lijst)
    gemiddelde = "{:.2f}".format(gemiddelde)
    return print(f"De gemiddelde inkomsten deze week zijn {gemiddelde} euro.")

def meervoudig(invoer_lijst):
    return print(laag_en_hoog(invoer_lijst))

def combinatie(invoer_lijst_2): 
    korte_lijst = meervoudig(invoer_lijst_2)
    result = mijn_functie_2(korte_lijst)
    return result
