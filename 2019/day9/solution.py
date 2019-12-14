from ..intcode import IntCode

inp = input('Insert your puzzle input:')

data = list(map(int, inp.split(',')))

r1 = IntCode(data.copy())
r2 = IntCode(data.copy())

out1 = r1.start(1)
out2 = r2.start(2)

print(f'Part 1 result is {out1}')
print(f'Part 2 result is {out2}')
