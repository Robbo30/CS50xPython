from pyfiglet import Figlet

inp = str(input("Input: "))
fontInp = input("Font: ")
if fontInp == "None":
    figlet = Figlet()
    figlet.getFonts()
    print(figlet.renderText(inp))
else:
    figlet = Figlet()
    figlet.getFonts()
    figlet.setFont(font = fontInp)
    print(figlet.renderText(inp))


