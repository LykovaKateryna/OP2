import func
text = func.inputText()
func.writeTextFile(text, "first.txt")
firstText = func.readTextFile("first.txt")
changedText = func.changeText(firstText)
func.writeTextFile(changedText, "last.txt")
print("Input file text:")
func.outputTextFile("first.txt")
print("Output file text:")
func.outputTextFile("last.txt")