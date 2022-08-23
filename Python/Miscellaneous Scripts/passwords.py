import secrets
import random

# macOS ships with a handy builtin word list. If you are on another OS you can substitute this file path for whatever comes with your OS.
words = open("/usr/share/dict/words").read().splitlines()

# This ugly line of code generates a random password with the form Word-Word-Word-WordNumberNumberNumberNumber
password = f"{random.choice(words).lower()}-{random.choice(words).lower()}-{random.choice(words).lower()}-{random.choice(words).lower()}{secrets.randbelow(10)}{secrets.randbelow(10)}{secrets.randbelow(10)}{secrets.randbelow(10)}"
print(f"Your password is: {password}")

num_words = len(words)
possibilities = (num_words**4) * (10**4)
print(
    f"That's amazing! I can't believe this happened! There was a one in {possibilities} chance of that happening!"
)
