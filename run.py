from graphs import *

command = ""
while True:
    command = raw_input("Enter a command: ")
    if command == "exit":
        break;
    name = raw_input("Enter a filename (no .json): ")
    filepath = "messages/" + name + ".json"
    if command == "all":
        allPlots(filepath)
    if command == "ratio":
        makeRatio(filepath)
        plt.show()
    if command == "weekday":
        makeWeekday(filepath)
        plt.show()
    if command == "month":
        makeMonth(filepath)
        plt.show()
    if command == "monyr":
        makeMonyr(filepath)
        plt.show()
    if command == "hours":
        makeHours(filepath)
        plt.show()
    if command == "days":
        makeAllDays(filepath)
        plt.show()
    if command == "words":
        makeWords(filepath)
        plt.show()
