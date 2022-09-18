import random
from time import sleep
import string

hello_list = ["H", "e", "l", "l", "o", " ", "W", "o", "r", "l", "d", "!"]
letter_list = list(string.ascii_letters + " " + string.punctuation)
progress = ""
candidate = ""

for i in range(len(hello_list)):
    while candidate != hello_list[i]:
        candidate = random.choice(letter_list)
        print(f"{progress}{candidate}", end="\r")
        sleep(0.05)

    progress += candidate
    candidate = ""

print()
