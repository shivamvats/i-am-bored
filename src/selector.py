from executor import *
from datetime import datetime
import random

def routineSelector():
    random.seed(a=datetime.now())
    routineIndex = random.randint(1, len(routineDict))
    return routineDict[routineIndex]

def main():
    routine = routineSelector()
    routine()

if __name__ == "__main__":
    main()
