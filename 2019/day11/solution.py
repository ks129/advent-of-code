#Importing
from ..intcode import IntCode
from collections import defaultdict
from PIL import Image

#Panels generator
def generate(data, init):
    dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    cpu = IntCode(data.copy())
    x, y, direction = 0, 0, 0
    panels = {(x, y): init}
    while not cpu.halted:
        cpu.add_input(panels[(x,y)] if (x,y) in panels else 0)
        cpu.run()
        color = cpu.output()
        dir = cpu.output()
        if not cpu.halted:
            panels[(x,y)] = color
            direction = ((direction + 1) if dir == 1 else (direction - 1 + len(dirs))) % len(dirs)
            x, y = x + dirs[direction][0], y + dirs[direction][1]
    return panels

#Image generator
def draw(panels):
    img = [[' ']*40 for _ in range(6)]
    for y in range(6):
        for x in range(40):
            if (x,y) in panels and panels[(x, y)] == 1:
                img[y][x] = '#'
    image = Image.new('RGB', (41, 7), 'black')
    pixels = image.load()
    for y, row in enumerate(img):
        for x, char in enumerate(row):
            pixels[(x,y)] = (255,255,255) if char == '#' else (0,0,0)
    image.save('output.png', 'PNG')
    return 'Output saved to output.png'

#Part 1 runner
def run1(data):
    panels = generate(data.copy(), 0)
    return len(panels)

#Part 2 runner
def run2(data):
    out = draw(generate(data.copy(), 1))
    return out

#Collecting data
data = list(map(int, input('Insert your puzzle input:').split(',')))

#Running
p1 = run1(data.copy())
p2 = run2(data.copy())

#Printing results
print(f'Part 1 result is {p1}')
print(f'Part 2 result is\n{p2}')
