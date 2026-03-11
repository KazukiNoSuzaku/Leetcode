# Given an array of strings words, return the words that can be typed using letters of the alphabet
# on only one row of American keyboard.

# Author: Kaustav Ghosh

class Solution(object):
    def findWords(self, words):
        rows = [set('qwertyuiop'), set('asdfghjkl'), set('zxcvbnm')]
        res = []
        for word in words:
            w = set(word.lower())
            if any(w <= row for row in rows):
                res.append(word)
        return res
