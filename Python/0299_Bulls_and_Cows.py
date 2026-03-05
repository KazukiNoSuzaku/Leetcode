# You are playing the Bulls and Cows game with your friend.
# You write down a secret number and ask your friend to guess what the number is.
# When your friend makes a guess, you provide a hint with the following info:
# - The number of "bulls", which are digits in the guess that are in the correct position.
# - The number of "cows", which are digits in the guess that are in your secret number but in
#   the wrong position.
# Given the secret number secret and your friend's guess guess, return the hint for your friend's guess.
# The hint should be formatted as "xAyB", where x is the number of bulls and y is the number of cows.

# Example 1:
# Input: secret = "1807", guess = "7810"
# Output: "1A3B"

# Example 2:
# Input: secret = "1123", guess = "0111"
# Output: "1A1B"

# Constraints:
# 1 <= secret.length, guess.length <= 1000
# secret.length == guess.length
# secret and guess consist of digits only.

# Author: Kaustav Ghosh

class Solution(object):
    def getHint(self, secret, guess):
        bulls = sum(s == g for s, g in zip(secret, guess))
        from collections import Counter
        sc = Counter(s for s, g in zip(secret, guess) if s != g)
        gc = Counter(g for s, g in zip(secret, guess) if s != g)
        cows = sum((sc & gc).values())
        return "{}A{}B".format(bulls, cows)
