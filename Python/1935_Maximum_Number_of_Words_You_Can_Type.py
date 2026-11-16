# Author: Kaustav Ghosh
# Problem: Maximum Number of Words You Can Type
# Approach: A word is typable exactly when none of its letters sits on a broken key, and the words are independent of one another, so the answer is just a count of the words that avoid the broken set. I put the broken letters in a set so each membership test is constant time, split the text on spaces, and count the words whose letters are all absent from that set, which costs one pass over the text.

class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        """
        :type text: str
        :type brokenLetters: str
        :rtype: int
        """
        broken = set(brokenLetters)
        return sum(1 for word in text.split(" ")
                   if all(letter not in broken for letter in word))
