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


with open("input.txt","r") as f:
    print(solve1(f))
