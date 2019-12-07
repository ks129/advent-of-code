#Getting file information
print('Insert input file location:')
inp = input()

#Part 1 Calculation
def calc1(data: int):
    result = int(data / 3) - 2
    return result

#Part 2 Calculation
def calc2(data: int):
    result1 = int(data / 3) - 2
    result = result1
    while result1 >= 3:
        result1 = int(result1 / 3) - 2
        if result1 < 0:
            result1 = 0
        result += result1
    return result

#Creating Result variables
result1 = 0
result2 = 0

#Opening file, running calcs
with open(inp, 'r') as f:
    for a in f:
        p1 = calc1(int(a))
        p2 = calc2(int(a))
        result1 += p1
        result2 += p2

#Printing results
print(f'Part 1 Result is {result1}')
print(f'Part 2 Result is {result2}')
