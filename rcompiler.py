import functions


class Compiler:

  def __init__(self):
    self.version = "v0.1"

  def compile(self, line, totalLines, co):
    c = line.split('-')
    x = c[1].split(" ")
    r = {
        "log": functions.standardOutput(c[1], co),
        "var": functions.createStandardVarriable(c[1], co),
        "math": functions.performStandardMath(c[1], co),
        "if": functions.createStandardIfStatement(c[1], totalLines, co),
        "input": functions.standardInputFunction(c[1], co),
        "function": functions.standardMethod(c[1], totalLines, co),
        "lower": functions.convertStringToLower(c[1], co),
        "upper": functions.convertStringToUpper(c[1], co),
        "call": functions.standardCall(c[1], totalLines, co),
        "repeat": functions.standardLoop(line, totalLines, c)
    }
    try:
      if "-" not in line and not line == "":
        r[x[0].lower()]
    except:
      print("Error, command unrecognized.")
