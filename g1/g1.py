
def solve1(f):
    #estrarre dati dal file
    righe = [list(map(int, line.split()))for line in f]
    colonne = list(zip(*righe))
    colonne = [list(col) for col in colonne]

    #ordinarli
    for col in colonne:
        col.sort()

    #fare le differenze e le somme
    somma = sum(abs(ele2-ele1) for ele1, ele2 in zip(colonne[0],colonne[1]))
    return somma

def solve2(f):
        #estrarre dati dal file
    righe = [list(map(int, line.split()))for line in f]
    colonne = list(zip(*righe))
    colonne = [list(col) for col in colonne]

    #ordinarli
    for col in colonne:
        col.sort()

    somma = 0
    for num in colonne[0]:
        # Contare quante volte 'num' appare in colonne[1]
        count = colonne[1].count(num)
        # Aggiungere num * count al punteggio
        somma += num * count

    return somma

with open("input.txt","r") as f:
    #print(solve1(f))
    print(solve2(f))
