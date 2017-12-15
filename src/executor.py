import feedparser
import pickle as pk
import subprocess
from datetime import date
import os

REL_READ_FILE = "../data/read_index"
REL_SRC_FILE = "../data/paulgraham_essays.rss"
dir = os.path.dirname(__file__)

def init():
    pass
    #setReadIndex(0)

def incrementIndex():
    index, date = getReadIndex()
    if index is None:
        setReadIndex(0)
    else:
        setReadIndex(index+1)

def setReadIndex(index):
    with open(os.path.join(dir, REL_READ_FILE), 'w') as f:
        pk.dump((index, date.today()), f)

def getReadIndex():
    try:
        with open(os.path.join(dir, REL_READ_FILE), 'r') as f:
            index, date  = pk.load(f)
        return (int(index), date)
    except IOError:
        # Return the first index.
        return (None, None)


def loadData(linkLocation):
    data = feedparser.parse(linkLocation)
    readIndex, readDate = getReadIndex()
    if readIndex is None:
        index = 0
    else:
        index = (readIndex + 1) % len(data.entries)
    return (data, index)


def executeRoutine():
    data, index = loadData(os.path.join(dir, REL_SRC_FILE))
    link = data.entries[index]['link']
    incrementIndex()

    print(link)
    # Open the link in a browser.
    subprocess.call(["xdg-open", link])
    # Show a notification.
    subprocess.call(["notify-send", "Routinizer", "Check you browser for" +
                    " today's essay."])
    loadCodingRoutine()

def loadRoutine1():
    """Solve a haskell problem using exercism."""
    subprocess.call(["notify-send", "i-am-bored", "Solve a haskell problem today"])
    os.system("gnome-terminal -e 'bash -c \"cd "
                "~/Documents/Coding/exercism/haskell;echo Switch to "
                "python3.6 env; exec bash\"'")

def loadRoutine2():
    """Read Terence Tao's blog."""
    subprocess.call(["notify-send", "i-am-bored", "Enjoy Terence Tao's blog today."])
    subprocess.call("xdg-open https://terrytao.wordpress.com/", shell=True)

def loadRoutine3():
    """Read about no free lunch theorem."""
    subprocess.call(["notify-send", "i-am-bored", "Read about the no free lunch theorem today."])
    subprocess.call("xdg-open http://no-free-lunch.org/", shell=True)

def loadRoutine4():
    """Read essays on rationality by Eliezer Yudkowsky, commonly called the sequences."""

    subprocess.call(["notify-send", "i-am-bored", "Read an essay from the sequences"])
    subprocess.call("xdg-open https://www.readthesequences.com/",
            shell=True)

routineDict = {
        1 : loadRoutine1,
        2 : loadRoutine2,
        3 : loadRoutine3,
        4 : loadRoutine4
        }

