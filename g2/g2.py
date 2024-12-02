
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
    # Estrarre i report dal file
    righe = [list(map(int, line.split())) for line in f]

    safe = 0
    for riga in righe:
        # Verifica se il report è sicuro
        differences = [abs(riga[i] - riga[i + 1]) for i in range(len(riga) - 1)]
        is_monotonic = all(riga[i] <= riga[i + 1] for i in range(len(riga) - 1)) or \
                       all(riga[i] >= riga[i + 1] for i in range(len(riga) - 1))
        if all(1 <= diff <= 3 for diff in differences) and is_monotonic:
            safe += 1
            continue

        # Verifica con il Problem Dampener
        for i in range(len(riga)):
            # Crea una versione ridotta della riga
            reduced_riga = riga[:i] + riga[i + 1:]
            differences_reduced = [abs(reduced_riga[j] - reduced_riga[j + 1]) for j in range(len(reduced_riga) - 1)]
            is_monotonic_reduced = all(reduced_riga[j] <= reduced_riga[j + 1] for j in range(len(reduced_riga) - 1)) or \
                                   all(reduced_riga[j] >= reduced_riga[j + 1] for j in range(len(reduced_riga) - 1))
            if all(1 <= diff <= 3 for diff in differences_reduced) and is_monotonic_reduced:
                safe += 1
                break

                
    return safe

with open("input.txt","r") as f:
    #print(solve1(f))
    print(solve2(f))