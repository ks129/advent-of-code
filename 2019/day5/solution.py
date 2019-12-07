#Getting puzzle input
print('Insert your puzzle input:')
inp = input()

#Generating lists
data = list(map(int, inp.split(',')))
data1 = list(map(int, inp.split(',')))

#Getting parameters
def parameters(op, command, counter):
    intr = list(str(command))

    parm = ([0]*(5 - len(str(command)))) + intr

    val1 = (op[counter + 1] if int(parm[2]) == 0 else (counter + 1))
    val2 = (op[counter + 2] if int(parm[1]) == 0 else (counter + 2))
    val3 = (op[counter + 3] if int(parm[0]) == 0 else (counter + 3))
    return val1, val2, val3


#Part 1 Main running
def run1(d):
    counter = 0
    input = 1
    while counter < len(d):
        intr = d[counter]
        opcode = int(str(intr)[-1])
        val1, val2, val3 = parameters(d, intr, counter)
        if opcode == 1:
            d[val3] = d[val1] + d[val2]
            counter += 4
        elif opcode == 2:
            d[val3] = d[val1] * d[val2]
            counter += 4
        elif opcode == 3:
            d[val1] = input
            counter += 2
        elif opcode == 99 or opcode == 4:
            if d[val1] != 0 and d[counter + 2] == 99:
                return d[val1]
            elif d[val1] != 0 and d[counter + 2] != 99:
                return f'Test failed with output {d[val1]}'
            counter += 2

#Part 2 Main running
def run2(d):
    counter = 0
    input = 5
    while counter < len(d):
        intr = d[counter]
        opcode = int(str(intr)[-1])
        val1, val2, val3 = parameters(d, intr, counter)
        if opcode == 1:
            d[val3] = d[val1] + d[val2]
            counter += 4
        elif opcode == 2:
            d[val3] = d[val1] * d[val2]
            counter += 4
        elif opcode == 3:
            d[val1] = input
            counter += 2
        elif opcode == 99 or opcode == 4:
            if d[val1] != 0 and d[counter + 2] == 99:
                return d[val1]
            elif d[val1] != 0 and d[counter + 2] != 99:
                return f'Test failed with output {d[val1]}'
            counter += 2
        elif opcode == 5:
            if d[val1] != 0:
                counter = d[val2]
            else:
                counter += 3
        elif opcode == 6:
            if d[val1] == 0:
                counter = d[val2]
            else:
                counter += 3
        elif opcode == 7:
            if d[val1] < d[val2]:
                d[val3] = 1
            else:
                d[val3] = 0
            counter += 4
        elif opcode == 8:
            if d[val1] == d[val2]:
                d[val3] = 1
            else:
                d[val3] = 0
            counter += 4
                

#Running parts
p1 = run1(data)
p2 = run2(data1)

#Printing results
print(f'Part 1 Result is {p1}')
print(f'Part 2 Result is {p2}')
