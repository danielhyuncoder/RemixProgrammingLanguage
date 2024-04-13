from rcompiler import Compiler

C = Compiler()
varriableMemoryStorage = {}
funcMemoryStorage = {}


def split(l):
  x = l.split(" ")
  return x


def convertSyntaxInString(c2):
  if "_" in c2:
    cx = c2.split("_")
    c2 = ""
    for e in cx:
      c2 += (e + " ")
    return c2


def convertStringToSyntax(c2):
  if " " in c2:
    cx = c2.split(" ")
    c2 = ""
    for e in range(len(cx)):
      if not e + 1 >= len(cx):
        c2 += (cx[e] + "_")
      else:
        c2 += cx[e]
    return c2


def standardLoop(line, totalLines, c):
  if split(line)[0].lower() == "repeat":
    try:
      count = int(split(line)[2])
      try:
        count = int(split(line)[2])
        try:
          r = int(split(line)[1])
        except:
          xx = split(line)[1].split("$")
          r = int(varriableMemoryStorage[xx[1]])
        cC = c - 1
        l = count + (c - 1)
        x = 0
        while x < r:
          while cC < l:
            cC += 1
            C.compile(totalLines[cC], totalLines, c)
          cC = c - 1
          x += 1
      except:
        print("Error on line, " + str(c) + " repeat number is not a string")
    except:
      print("Error on line, " + str(c) + " count is not a string")


def convertStringToUpper(line, c):
  if split(line)[0].lower() == "upper":
    try:
      m = str(varriableMemoryStorage[split(line)[1]])
      varriableMemoryStorage[split(line)[1]] = m.upper()
    except:
      print(
          "Cannot uppercase string due to incorrect data types or the varriable mentioned is undefined on line "
          + str(c) + ".")


def convertStringToLower(line, c):
  if split(line)[0].lower() == "lower":
    try:
      m = str(varriableMemoryStorage[split(line)[1]])
      varriableMemoryStorage[split(line)[1]] = m.lower()
    except:
      print(
          "Cannot lowercase string due to incorrect data types or the varriable mentioned is undefined on line "
          + str(c) + ".")


def standardMethod(line, totalLines, c):
  if split(line)[0].lower() == "function":
    try:
      fN = split(line)[1].split('\n')[0]
      funcMemoryStorage[fN] = c
    except:
      print("Error on line: " + str(c) +
            ". Function does not have enough parameters.")


def standardCall(line, totalLines, c):
  if split(line)[0].lower() == "call":
    try:
      r = funcMemoryStorage[split(line)[1].split('\n')[0]]
      try:
        r2 = r - 1
        rr = r2
        l = totalLines[r - 1]
        x = l.split(" ")[2]
        x = int(x.split("\n")[0])
        while r2 < (x + rr):
          r2 += 1
          C.compile(totalLines[r2], totalLines, r2)

      except:
        print("Error on line: " + str(c) +
              ". Function mentioned is unspecified.")
    except:
      print("Error on line: " + str(c) +
            ". Function mentioned is unspecified.")


def standardOutput(line, c):
  if split(line)[0].lower() == "log":
    if "$" in split(line)[1]:
      try:
        if "_" in varriableMemoryStorage[split(line)[1].split("$")[1].split(
            "\n")[0]]:
          print(
              convertSyntaxInString(varriableMemoryStorage[split(
                  line)[1].split("$")[1].split("\n")[0]]))
        else:
          print(varriableMemoryStorage[split(line)[1].split("$")[1]])
      except:
        try:
          print(varriableMemoryStorage[split(line)[1].split("$")[1].split("\n")
                                       [0]])
        except:
          print("Error recognizing varriable on line " + str(c))
    else:
      try:
        if convertSyntaxInString(split(line)[1]) != None:
          print(convertSyntaxInString(split(line)[1]))
        else:
          print(split(line)[1])
      except:
        try:
          print(split(line)[1])
        except:
          print("Unexpected Error on line: " + str(c))


def standardInputFunction(line, c):
  if split(line)[0].lower() == "input":
    try:
      i = input("")
      try:
        if " " in i:
          varriableMemoryStorage[split(line)[1].split("\n")
                                 [0]] = convertStringToSyntax(i)
        else:
          varriableMemoryStorage[split(line)[1].split("\n")[0]] = i
      except:
        try:
          varriableMemoryStorage[split(line)[1].split("\n")[0]] = float(i)
        except:
          varriableMemoryStorage[split(line)[1].split("\n")[0]] = int(i)

    except:
      print("Varriable mentioned does not exist.")


def createStandardIfStatement(line, lines, c):
  if split(line)[0].lower() == "if":
    x = split(line)
    c1 = None
    c2 = None
    o = x[2]
    if "$" in x[1]:
      m = x[1].split("$")
      try:
        c1 = varriableMemoryStorage[m[1]]
      except:
        print("Error on line " + str(c) +
              "varriable mentioned does not exist.")
      try:
        c1 = float(c1)
      except:
        try:
          c1 = int(c1)
        except:
          c1 = c1
    else:
      try:
        c1 = float(x[1])
      except:
        try:
          c1 = int(x[1])
        except:
          c1 = x[1]
    if "$" in x[3]:
      m = x[3].split("$")
      try:
        c2 = varriableMemoryStorage[m[1]]
      except:
        print("Error on line, " + str(c) +
              " varriable mentioned does not exist.")
      try:
        c2 = float(c2)
      except:
        try:
          c2 = int(c2)
        except:
          c2 = c2
    else:
      try:
        c2 = float(x[3])
      except:
        try:
          c2 = int(x[3])
        except:
          c2 = x[3]
    try:
      if "_" in c2:
        c2 = convertSyntaxInString(c2)
      if "_" in c1:
        c1 = convertSyntaxInString(c1)
    except:
      print("")
    lineC = x[4]
    try:
      lineC = int(lineC)
    except:
      print("Error on line " + str(c) +
            ": There must be an integar as the line count in the if statement")
    statementIsTrue = False
    if x[2] == "==" and c1 == c2:
      statementIsTrue = True
    elif x[2] == "!=" and not c1 == c2:
      statementIsTrue = True
    if statementIsTrue:
      mC = c
      while (mC) < (c + lineC):
        C.compile(lines[mC], lines, c)
        mC += 1


def createStandardVarriable(line, c):
  if split(line)[0].lower() == "var":
    varriableMemoryStorage[split(line)[1]] = split(line)[3]


def performStandardMath(line, c):
  if split(line)[0].lower() == "math":
    v1 = []
    v2 = []
    if "$" in split(line)[1].lower():
      try:
        v1.append(split(line)[1].lower())
        v1.append(varriableMemoryStorage[split(line)[1].split("$")[1]])
      except:
        print("Error recognizing varriable on line " + str(c))
    else:
      v1.append(False)
      v1.append(split(line)[1].lower())
    if "$" in split(line)[3].lower():
      try:
        v2.append(split(line)[3].lower())
        v2.append(varriableMemoryStorage[split(line)[3].split("$")[1]])
      except:
        print("Error recognizing varriable on line " + str(c))
    else:
      v2.append(False)
      v2.append(split(line)[3].lower())
    try:
      v1[1] = float(v1[1])
      v2[1] = float(v2[1])
      if split(line)[2].lower() == "+":
        if v1[0]:
          varriableMemoryStorage[v1[0].split("$")[1]] = str(v1[1] + v2[1])
        else:
          print(v1[1] + v2[1])
      if split(line)[2].lower() == "-":
        if v1[0]:
          varriableMemoryStorage[v1[0].split("$")[1]] = str(v1[1] - v2[1])
        else:
          print(v1[1] - v2[1])
      if split(line)[2].lower() == "*":
        if v1[0]:
          varriableMemoryStorage[v1[0].split("$")[1]] = str(v1[1] * v2[1])
        else:
          print(v1[1] * v2[1])
      if split(line)[2].lower() == "/":
        if v1[0]:
          varriableMemoryStorage[v1[0].split("$")[1]] = str(v1[1] / v2[1])
        else:
          print(v1[1] / v2[1])
    except:
      print(
          "Math operation needs at least an integer number to perform on line "
          + str(c) + ".")
