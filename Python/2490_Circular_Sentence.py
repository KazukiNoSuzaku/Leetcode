class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split()
        n = len(words)
        return all(words[i][-1] == words[(i + 1) % n][0] for i in range(n))
