from executor import *
from datetime import datetime
import random
import sys

def randomRoutineSelector():
    random.seed(a=datetime.now())
    routineIndex = random.randint(1, len(routineDict))
    return routineDict[routineIndex]

def runCommand(command):
    if command == "list":
        print("Following routines are avaiable.")
        for index, desc in routineDescriptions.iteritems():
            print("%d - "%index + desc)
    else:
        raise NotImplementedError

def runCommandWithArgs(command, args):
    if command == "run":
        index = int(args[0])
        routine = routineDict[index]
        routine()
    else:
        raise NotImplementedError

def main():
    argv = sys.argv
    if len(argv) == 1:
        routine = randomRoutineSelector()
        routine()
    elif len(argv) == 2:
        # Command with no argument.
        runCommand(argv[1])
    elif len(argv) == 3:
        # Command with an argument.
        runCommandWithArgs(argv[1], argv[2:])
    else:
        raise NotImplementedError

if __name__ == "__main__":
    main()
