from executor import *
import random

def routineSelector():
    routineIndex = random.randint(1, len(routineDict))
    return routineDict[routineIndex]

def main():
    routine = routineSelector()
    routine()

if __name__ == "__main__":
    main()
