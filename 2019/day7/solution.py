#Module imports
import itertools

#IntCode Computer import
from intcode import IntCode

#Part 1 Runner
def run1(data):
    result = 0
    perms = itertools.permutations(range(5))
    for perm in perms:
        amp = 0
        for phase in perm:
            cpu = IntCode(data.copy(), [phase, amp])
            cpu.run()
            amp = cpu.outputs[-1]
        result = max(result, amp)
    return result

#Part 2 Runner
def run2(data):
    result = 0
    for phases in itertools.permutations(range(5, 10)):
        cpu = []
        for phase in phases:
            cpu.append(IntCode(data.copy(), [phase]))
        input = 0
        while not cpu[0].halted:
            for machine in cpu:
                machine.add_input(input)
                machine.run()
                input = machine.outputs[-1]
        result = max(result, input)
    return result
    
#Collecting data
data = list(map(int, input('Insert your puzzle input:').split(',')))

#Running runners
p1 = run1(data.copy())
p2 = run2(data.copy())

#Printing results
print(f'Part 1 result is {p1}')
print(f'Part 2 result is {p2}')
