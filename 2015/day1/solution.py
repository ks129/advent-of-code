import re

#Getting puzzle input
print('Insert your puzzle input:')
inp = input()

#Part 1 Generator
def part1(inp):
    #Finding counts
    o = re.findall(r'\(', inp)
    c = re.findall(r'\)', inp)

    result = len(o) - len(c)
    return result

#Part 2 Generator
def part2(inp):
    characters = 0
    floor = 0
    basement = False
    for i in inp:
        if i == '(':
            floor += 1
        elif i == ')':
            floor -= 1
        characters += 1
        if floor < 0:
            if not basement:
                basement = True
                break
    return characters

#Running funcs
p1 = part1(inp)
p2 = part2(inp)

#Printing results
print(f'Part 1 result is {p1}')
print(f'Part 2 result is {p2}')
