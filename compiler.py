import functions


class Compiler:

  def compile(self, line, totalLines, c):
    line = line.split("\n")[0]
    r = {
        "log": functions.standardOutput(line, c),
        "var": functions.createStandardVarriable(line, c),
        "math": functions.performStandardMath(line, c),
        "if": functions.createStandardIfStatement(line, totalLines, c),
        "input": functions.standardInputFunction(line, c),
        "function": functions.standardMethod(line, totalLines, c),
        "lower": functions.convertStringToLower(line, c),
        "upper": functions.convertStringToUpper(line, c),
        "call": functions.standardCall(line, totalLines, c),
        "repeat": functions.standardLoop(line, totalLines, c)
    }
    x = line.split(' ')
    try:
      if "-" not in line and not line == "":
        r[x[0].lower()]
    except:
      if "-" not in line:
        print("Error, command unrecognized.")
