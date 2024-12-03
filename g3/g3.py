
import re
def solve1(f):
    #estrarre dati dal file
    righe = re.findall(r"mul\(\d+,\d+\)",f.read())
    sum = 0
    for mul in righe:
        mul = re.sub(r'mul\(([^)]*)\)', r'\1', mul)
        mul1, mul2 = mul.split(",")
        mul1 = int(mul1)
        mul2 = int(mul2)
        sum += mul1*mul2

    return sum

def solve2(f):
    #estrarre dati dal file
    righe = re.findall(r"mul\(\d+,\d+\)",f.read())
    return righe

with open("input.txt","r") as f:
    print(solve1(f))
    #print(solve2(f))