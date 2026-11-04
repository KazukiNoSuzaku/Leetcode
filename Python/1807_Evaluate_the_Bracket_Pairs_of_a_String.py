# Author: Kaustav Ghosh
# Problem: Evaluate the Bracket Pairs of a String
# Approach: The brackets never nest, so one left-to-right scan is enough: text outside a pair is copied through, and the characters between an opening and a closing bracket are collected as a key and then replaced by its value, or by a question mark when the key is unknown. The knowledge list becomes a dictionary first so each lookup is constant time rather than a search, and the output is assembled as a list of pieces and joined once, which keeps the whole pass linear even for strings of a hundred thousand characters.

class Solution(object):
    def evaluate(self, s, knowledge):
        """
        :type s: str
        :type knowledge: List[List[str]]
        :rtype: str
        """
        values = dict(knowledge)
        pieces = []
        key = None
        for character in s:
            if character == "(":
                key = []
            elif character == ")":
                pieces.append(values.get("".join(key), "?"))
                key = None
            elif key is None:
                pieces.append(character)
            else:
                key.append(character)
        return "".join(pieces)
