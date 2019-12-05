#Getting input
print('Enter your puzzle input:')
input = input()

#Generating list
data = input.split(',')

#Main proccessor
def process(inp):
  for i in range(0, len(inp), 4):
    opcode = inp[i]
    val1, val2 = inp[inp[index + 1]], inp[inp[index + 1]]
    if opcode == 99:
      return inp[0]
    elif opcode == 1:
      inp[inp[i + 3]] = val1 + val2
    elif opcode == 2:
      inp[inp[i + 3]] = val1 * val2
    return inp[0]
  
#Running
result = process(data)

#Printing output
print(f'Result: {result}')
