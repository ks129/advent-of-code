#Collect data
print('Insert start number (your puzzle input part before -):')
start = input()
print('Insert ending number (your puzzle input part after -):')
end = input()

#Generating list
numbers = map(str, range(start, end))

#Checking Day 4 Part 1 Requirements
def check1(num):
    decrease = False
    repeat = 0

    for r in range(len(num)):
        if r > 0 and num[r] == num[r - 1]:
            repeat += 1
        if r > 0 and num[r - 1] > num[r]:
            decrease = True
    return decrease is False and repeat > 0

#Checking Day 4 Part 2 Requirements
def check2(num):
    repeat = 0
    double = False
    for n1, n2 in zip(num, num[1:]):
        if n1 > n2:
            return False
        elif n1 == n2:
            repeat += 1
        else:
            if repeat == 1:
                double = True
            repeat = 0

    if repeat == 1:
        double = True
    return double

#Day 4
count1 = 0
count2 = 0
for num in numbers:
    p1 = check1(num)
    p2 = check2(num)
    if p1:
        count1 += 1
    if p2:
        count2 += 1

print(f"Result for Part 1: {count1}")
print(f"Result for Part 2: {count2}")
