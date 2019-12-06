#Getting file name
print('Insert location and name of input file:')
file = input()

#Part 1 Calculations
def calc1(data):
    d = data.split('x')

    result = 2 * int(d[0]) * int(d[1]) + 2 * int(d[1]) * int(d[2]) + 2 * int(d[2]) * int(d[0])
    extra = [int(d[0]) * int(d[1]), int(d[1]) * int(d[2]), int(d[2]) * int(d[0])]
    extra.sort()
    result += extra[0]

    return result

#Part 2 Calculations
def calc2(data):
    d = data.split('x')

    r1 = 2 * min(int(d[0]) + int(d[1]), int(d[1]) + int(d[2]), int(d[2]) + int(d[0]))
    r2 = int(d[0]) * int(d[1]) * int(d[2])
    result = r1 + r2
    return result

#Creating counters
result1 = 0
result2 = 0

#Opening file and looping lines, calcs
with open(file, 'r') as f:
    for i in f:
        res1 = calc1(i)
        res2 = calc2(i)
        result1 += res1
        result2 += res2

#Print results
print(f'Part 1 result is {result1}')
print(f'Part 2 result is {result2}')
