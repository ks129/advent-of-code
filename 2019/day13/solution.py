#Importing standart IntCode VM
from intcode import IntCode

#Getting Special IntCode Computer values
def get_values(data, vals, counter, relative):
    lock = [1, 2, 3, 7, 8]
    opcode = data[counter] % 100
    mods = data[counter] // 100
    values = []
    for i in range(1, vals + 1):
        val = data[counter + i]
        mode = mods % 10
        mods //= 10
        if i < vals or opcode not in lock:
            if mode == 0:
                val = data[val]
            elif mode == 2:
                val = data[relative + val]
        elif mode == 2:
            val += relative
        values.append(val)
    return values

#Special IntCode Computer for Part 2
def sp_intcode(data, input):
    input = iter(input)
    data.extend([0] * 99999)
    counter = 0
    relative = 0

    while 1:
        opcode = data[counter] % 100

        if opcode == 99:
            break
        elif opcode == 1:
            val1, val2, val3 = get_values(data, 3, counter, relative)
            data[val3] = val1 + val2
            counter += 4
        elif opcode == 2:
            val1, val2, val3 = get_values(data, 3, counter, relative)
            data[val3] = val1 * val2
            counter += 4
        elif opcode == 3:
            val1, = get_values(data, 1, counter, relative)
            data[val1] = next(input)
            counter += 2
        elif opcode == 4:
            val1, = get_values(data, 1, counter, relative)
            yield val1
            counter += 2
        elif opcode == 5:
            val1, val2 = get_values(data, 2, counter, relative)
            if val1:
                counter = val2
            else:
                counter += 3
        elif opcode == 6:
            val1, val2 = get_values(data, 2, counter, relative)
            if not val1:
                counter = val2
            else:
                counter += 3
        elif opcode == 7:
            val1, val2, val3 = get_values(data, 3, counter, relative)
            data[val3] = int(val1 < val2)
            counter += 4
        elif opcode == 8:
            val1, val2, val3 = get_values(data, 3, counter, relative)
            data[val3] = int(val1 == val2)
            counter += 4
        elif opcode == 9:
            val1, = get_values(data, 1, counter, relative)
            relative += val1
            counter += 2
        else:
            print('Invalid INTCODE OPCODE!')
            break

#Part 1 runner
def run1(data):
    cpu = IntCode(data.copy())
    result = 0
    tiles = {
        0: ' ',
        1: '#',
        2: '*',
        3: '_',
        4: 'O'
    }
    grid = {}
    while not cpu.halted:
        cpu.run()
    for i in range(0, len(cpu.outputs), 3):
        grid[(cpu.outputs[i], cpu.outputs[i+1])] = cpu.outputs[i+2]
    for ig, g in grid.items():
        if g == 2:
            result += 1
    return result, len(grid), grid

#Getting input for part 2
def get_input(screen):
    ball = [key for key, val in screen.items() if val == 4][0][0]
    paddle = [key for key, val in screen.items() if val == 3][0][0]
    if paddle < ball:
        return 1
    elif paddle > ball:
        return -1
    return 0

#Create initial Part 2 screen
def create(screen, size, cpu, score):
    for _ in range(size+1):
        x, y, tile = next(cpu), next(cpu), next(cpu)
        if x == -1 and y == 0:
            score = tile
        else:
            screen[(x, y)] = tile

#Modify Part 2 screen
def modify(screen, cpu, score):
    val = None
    while val != 4:
        try:
            x = next(cpu)
        except StopIteration:
            break
        y, val = next(cpu), next(cpu)
        if x == -1 and y == 0:
            score = val
        else:
            screen[(x,y)] = val
    return score

#Part 2 runner
def run2(data, size, screen):
    data[0] = 2
    inputs = []
    cpu = sp_intcode(data, inputs)
    score = 0
    create(screen, size, cpu, score)
    while True:
        if list(screen.values()).count(2) == 0:
            break
        inputs.append(get_input(screen))
        score = modify(screen, cpu, score)
    return score
        
#Collecting puzzle input
data = list(map(int, input('Insert your puzzle input:').split(',')))

#Running runners
p1, size, screen = run1(data.copy())
p2 = run2(data.copy(), size, screen)

#Printing outputs
print(f'Part 1 result is {p1}')
print(f'Part 2 result is {p2}')
