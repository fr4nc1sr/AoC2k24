
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
    # Extract relevant instructions
    righe = re.findall(r"mul\(\d+,\d+\)|don't\(\)|do\(\)", f.read())
    
    # Initialize state
    enabled = True  # Multiplications are enabled by default
    total_sum = 0

    # Process each instruction in sequence
    for instruction in righe:
        if instruction == "do()":
            enabled = True  # Enable future mul instructions
        elif instruction == "don't()":
            enabled = False  # Disable future mul instructions
        elif "mul" in instruction and enabled:
            # Extract the numbers and calculate the product
            mul_values = re.findall(r"\d+", instruction)
            a, b = map(int, mul_values)
            total_sum += a * b

    return total_sum

with open("input.txt","r") as f:
    #print(solve1(f))
    print(solve2(f))