from collections import deque

class IntCode:
  def __init__(self, data, input=[]):
    self.memory = data
    self.input = deque(input)
    self.counter = 0
    self.relative = 0
    self.outputs = []
    self.halted = False
    self.need_input = False
    self.memory.extend([0] * 99999)

  def add_input(self, input):
    self.need_input = False
    self.input.append(input)

  def run(self):
    while self.memory[self.counter] != 99:
      opcode = self.memory[self.counter] % 100

      if opcode == 1:
        self.set_value(3, self.get_value(1) + self.get_value(2))
        self.counter += 4
      elif opcode == 2:
        self.set_value(3, self.get_value(1) * self.get_value(2))
        self.counter += 4
      elif opcode == 3:
        if len(self.input) == 0:
          self.need_input = True
          break
        self.set_value(1, self.input.popleft())
        self.counter += 2
      elif opcode == 4:
        self.outputs.append(self.get_value(1))
        self.counter += 2
      elif opcode == 5:
        if self.get_value(1):
          self.counter = self.get_value(2)
        else:
          self.counter += 3
      elif opcode == 6:
        if not self.get_value(1):
          self.counter = self.get_value(2)
        else:
          self.counter += 3
      elif opcode == 7:
        self.set_value(3, int(self.get_value(1) < self.get_values(2)))
        self.counter += 4
      elif opcode == 8:
        self.set_value(3, int(self.get_value(1) == self.get_value(2)))
        self.counter += 4
      elif opcode == 9:
        self.relative += self.get_value(1)
        self.counter += 2
      else:
        print(f'Invalid OPCode {opcode}')
        break
    if not self.need_input:
      self.halted = True

  def get_mode(self, val):
    return (self.memory[self.counter] // (10**(val + 1))) % 10

  def set_value(self, location, val):
    if self.get_mode(location) == 2:
      self.memory[self.relative+self.memory[self.counter+location]] = val
    elif self.get_mode(location) == 1:
      self.memory[self.counter+location] = val
    else:
      self.memory[self.memory[self.counter+location]] = val

  def get_value(self, location):
    if self.get_mode(location) == 2:
      return self.memory[self.relative+self.memory[self.counter+location]]
    elif self.get_mode(location) == 1:
      return self.memory[self.counter+location]
    else:
      return self.memory[self.memory[self.counter+location]]
