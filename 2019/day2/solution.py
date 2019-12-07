#Getting puzzle input
print('Insert your puzzle input:')
inp = input()

#Generating lists
data1 = inp.split(',')
data2 = inp.split(',')

#Main calc
def run(d, noun, verb):
    d[1] = noun
    d[2] = verb
    for i in range(0, len(d), 4):
        if int(d[i]) == 1:
            loc1 = int(d[i + 1])
            loc2 = int(d[i + 2])
            val1 = int(d[loc1])
            val2 = int(d[loc2])
            d[int(d[i + 3])] = val1 + val2
        elif int(d[i]) == 2:
            loc1 = int(d[i + 1])
            loc2 = int(d[i + 2])
            val1 = int(d[loc1])
            val2 = int(d[loc2])
            d[int(d[i + 3])] = val1 * val2
        elif int(d[i]) == 99:
            break
    return int(d[0])
    
#Running part 1
def gen1(d):
    result = run(d, 12, 2)
    return result

#Running part 2
def gen2(d):
    for n in range(100):
        for v in range(100):
            da = d.copy()
            res = run(da, n, v)

            if res == 19690720:
                return 100 * n + v

#Running parts
p1 = gen1(data1)
p2 = gen2(data2)

#Printing results
print(f'Part 1 Result is {p1}')
print(f'Part 2 Result is {p2}')
