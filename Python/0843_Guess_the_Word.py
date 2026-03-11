# Guess secret word using min-max strategy minimizing worst case.

# Author: Kaustav Ghosh

import random

class Solution(object):
    def findSecretWord(self, wordlist, master):
        def match(a, b):
            return sum(x == y for x, y in zip(a, b))
        for _ in range(10):
            guess = random.choice(wordlist)
            m = master.guess(guess)
            wordlist = [w for w in wordlist if match(w, guess) == m]
