from enum import IntEnum

class OPCode(IntEnum):
  add = 1
  multi = 2
  input = 3
  output = 4
  jump_true = 5
  jump_false = 6
  less = 7
  equal = 8
  inc_rl = 9
  halt = 99

class IntCode:
  def __init__(self, memory, ph=None):
    self.memory = memory
    self.memory.extend([0] * 999999)
    self.relative = 0
    self.counter = 0
    self.intput = []
    self.outputs = []
    if ph:
      self.sparam(1, ph)
      self.counter += 2

  def start(self, intput):
    if intput is not None:
      self.intput.append(intput)

    while self.memory[self.counter] != OPCode.halt:
      op = self.memory[self.counter] % 100

      if len(str(op)) == 2:
        op = int(str(op)[len(str(op)) - 1])

      if op == OPCode.add:
        self.sparam(3, self.param(1) + self.param(2))
        self.counter += 4
      elif op == OPCode.multi:
        self.sparam(3, self.param(1) * self.param(2))
        self.counter += 4
      elif op == OPCode.input:
        if len(self.intput) == 0:
          return
        a = self.intput.pop(0)
        self.sparam(1, int(a))
        self.counter += 2
      elif op == OPCode.output:
        out = int(self.param(1))
        self.counter += 2
        self.outputs.append(out)
      elif op == OPCode.jump_true:
        if self.param(1):
          self.counter = self.param(2)
        else:
          self.counter += 3
      elif op == OPCode.jump_false:
        if not self.param(1):
          self.counter = self.param(2)
        else:
          self.counter += 3
      elif op == OPCode.less:
        self.sparam(3, self.param(1) < self.param(2))
        self.counter += 4
      elif op == OPCode.equal:
        self.sparam(3, self.param(1) == self.param(2))
        self.counter += 4
      elif op == OPCode.inc_rl:
        self.relative += self.param(1)
        self.counter += 2
    return self.outputs[0]

  @property
  def run(self):
    return self.memory[self.counter] != 99

  def param(self, val):
    if self.mode(val) == 2:
      return self.memory[self.relative + self.memory[self.counter + val]]
    elif self.mode(val) == 1:
      return self.memory[self.counter + val]
    else:
      return self.memory[self.memory[self.counter + val]]

  def sparam(self, loc, val):
    if self.mode(loc) == 2:
      self.memory[self.relative + self.memory[self.counter + loc]] = val
    elif self.mode(loc) == 1:
      self.memory[self.counter + loc] = val
    else:
      self.memory[self.memory[self.counter + loc]] = val
  def mode(self, val):
    return (self.memory[self.counter] // (10 ** (val + 1))) % 10
