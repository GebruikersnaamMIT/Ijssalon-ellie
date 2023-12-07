from helper import onderstreep

uitvoer = onderstreep("AANBIEDING")
uitvoer.append("Aardbeienijs, emmertje van 5 liter: 5 euro")
uitvoer.append("Slagroom, spuitbus van 1 liter: 2 euro")
print()

for i in range(len(uitvoer)):
    print(uitvoer[i])
    
'''
#Alternatief: 

for el in uitvoer:
    print(el)

'''
