#Getting input
print('Enter your puzzle input:')
input = input()

#Generating list
data = input.split(',')

#Main proccessor
def process(in):
  for i in range(0, len(in), 4):
    opcode = in[i]
    val1, val2 = data[data[index + 1]], data[data[index + 1]]
    if opcode == 99:
      return data[0]
    elif opcode == 1:
      data[data[i + 3]] = val1 + val2
    elif opcode == 2:
      data[data[i + 3]] = val1 * val2
    return data[0]
  
#Running
result = process(data)

#Printing output
print(f'Result: {result}')
