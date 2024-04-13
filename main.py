from compiler import Compiler

C = Compiler()

while True:
  x = str(input("(>>>) "))
  try:
    file = open(x, "r")
    f = []
    c = 0
    for line in file:
      f.append(line)
    for line in f:
      c += 1
      C.compile(line, f, c)
    file.close()
  except:
    print("File does not exist")
