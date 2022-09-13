import random
from time import sleep

hello_list = ["H", "e", "l", "l", "o", " ", "W", "o", "r", "l", "d", "!"]
letter_list = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
    " ",
    "!",
]
progress = ""
candidate = ""

for i in range(len(hello_list)):
    while candidate != hello_list[i]:
        candidate = random.choice(letter_list)
        print(f"{progress}{candidate}", end="\r")
        sleep(0.1)

    progress += candidate
    candidate = ""

print()
