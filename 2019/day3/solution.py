#Collecting puzzle inout
print('Enter first part of your puzzle input:')
in1 = input()
print('Enter second part of your puzzle input:')
in2 = input()

#Walking/Moving
def move_on(movel):
    x = 0
    y = 0
    for action in movel.split(','):
        dir = action[0]
        amount = int(action[1:])
        for i in range(amount):
            yield (x, y)
            if dir == 'L':
                x -= 1
            elif dir == 'U':
                y += 1
            elif dir == 'R':
                x += 1
            elif dir == 'D':
                y -= 1
    yield (x, y)

#Part 1 Generator
def calc1(moves1, moves2):
    res = None
    fielding = {}
    counter = 0
    for move in (moves1, moves2):
        counter += 1
        for x_loc, y_loc in move_on(move):
            tr = x_loc or y_loc
            if tr and fielding.setdefault((x_loc, y_loc), counter) != counter:
                man = abs(x_loc) + abs(y_loc)
                if res is None or res > man:
                    res = man
    return res

#Part 2 Generator
def calc2(moves1, moves2):
    res = None
    fielding = {}
    dis_tot = {}
    counter = 0
    for move in (moves1, moves2):
        counter += 1
        dis = 0
        for x_loc, y_loc in move_on(move):
            check = not x_loc and not y_loc
            if check:
                pass
            elif (x_loc, y_loc) not in fielding:
                fielding[(x_loc, y_loc)] = counter
                dis_tot[(x_loc, y_loc)] = dis
            elif fielding[(x_loc, y_loc)] != counter:
                o = dis_tot[(x_loc, y_loc)]
                if res is None or res > o + dis:
                    res = o + dis
                if o > dis:
                    fielding[(x_loc, y_loc)] = counter
                    dis_tot[(x_loc, y_loc)] = dis
            dis += 1
    return res
                
    
#Running generators
p1 = calc1(in1, in2)
p2 = calc2(in1, in2)

#Printing result
print(f'Part 1 result is {p1}')
print(f'Part 2 result is {p2}')
