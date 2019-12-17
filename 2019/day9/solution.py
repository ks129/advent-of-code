#Import IntCode Computer
from ..intcode import IntCode

#Collect puzzle input
inp = input('Insert your puzzle input:')

#Generate list of data
data = list(map(int, inp.split(',')))

#Creating IntCode Computers
r1 = IntCode(data.copy(), [1])
r2 = IntCode(data.copy(), [2])

#Running IntCode Computers
r1.run()
r2.run()

#Getting outputs
p1 = r1.outputs[-1]
p2 = r2.outputs[-1]

#Printing outputs
print(f'Part 1 result is {p1}')
print(f'Part 2 result is {p2}')
