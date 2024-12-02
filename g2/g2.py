
def solve1(f):
    #estrarre dati dal file
    righe = [list(map(int, line.split()))for line in f]

    #fare le differenze 
    safe = 0
    for riga in righe:
        ord = riga==sorted(riga)
        ord_contr = riga==sorted(riga, reverse=True)
        if ord or ord_contr:
            # Controllare se tutte le differenze sono tra 1 e 3
            differenze = [abs(riga[i] - riga[i + 1]) for i in range(len(riga) - 1)]
            if all(1 <= diff <= 3 for diff in differenze):
                safe += 1
    return safe

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
    print(solve1(f))
    #print(solve2(f))
    #solve1(f)
    #print("end")