#Collecting file name
print('Insert input file location and/or name:')
inp = input()

#Creating Planet class
class Planet():
    def __init__(self, planet, higher):
        self.planet = planet
        self.higher = higher
        self.childs = []

    def orbits(self):
        if self.higher == None:
            return 0

        return 1 + self.higher.orbits()

    def __str__(self):
        return self.planet

    def __repr__(self):
        childs = [child.name for child in self.childs]
        return f'{str(childs)} > {self.planet} > {self.higher}'

#Main generator
def generator(inp):
    planets = []
    with open(inp) as f:
        for i in f:
            b_name, planet = i.rstrip().split(')')
            sat = None
            b = None
            for p in planets:
                if planet == p.planet:
                    sat = p
                if b_name == p.planet:
                    b = p

            if sat != None and b != None:
                sat.higher = b
                b.childs.append(sat)
            elif sat != None and b == None:
                b = Planet(b_name, None)
                b.childs.append(sat)
                sat.higher = b
                planets.append(b)
            elif sat == None and b != None:
                sat = Planet(planet, b)
                b.childs.append(sat)
                planets.append(sat)
            elif sat == None and b == None:
                b = Planet(b_name, None)
                sat = Planet(planet, b)
                b.childs.append(sat)
                planets.append(b)
                planets.append(sat)
    return planets

#Part 1 Runner
def run1(inp):
    result = 0
    get_res = generator(inp)
    for p in get_res:
        result += p.orbits()
    return result

#Part 2 Runner
def run2(inp):
    result = 0
    res = generator(inp)
    for i in res:
        if i.planet == 'YOU':
            you = i
    s = [you]
    q = [you]
    p = []
    while len(q) > 0:
        i = q[-1]
        if i == None:
            q.pop()
            continue

        while len(p) != 0:
            if i not in p[-1].childs and i != p[-1].higher:
                p.pop()
            else:
                break
        if len(i.childs) != 0:
            p.append(i)

        na = [a.planet for a in i.childs]
        if "SAN" in na:
            break

        q.pop()

        if i.higher not in s:
            q.append(i.higher)
            s.append(i.higher)
        for c in i.childs:
            if c not in s:
                q.append(c)
                s.append(c)
    return len(p) - 1

#Running runners
p1 = run1(inp)
p2 = run2(inp)

#Printing results
print(f'Part 1 result is {p1}')
print(f'Part 2 result is {p2}')
