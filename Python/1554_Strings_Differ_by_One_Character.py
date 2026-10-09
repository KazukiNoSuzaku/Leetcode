# Author: Kaustav Ghosh
# Problem: Strings Differ by One Character
# Approach: Two words differ at exactly one index precisely when blanking that index makes them identical, and the words are distinct so an identical blanked pair cannot differ anywhere else. Checking each index with a rolling hash avoids rebuilding the blanked word, since a word's hash minus its character's weight at that position is the blanked hash; matches are confirmed character by character so a hash collision cannot pass

class Solution(object):
    def differByOne(self, dict):
        """
        :type dict: List[str]
        :rtype: bool
        """
        words = dict
        width = len(words[0])
        MOD = (1 << 61) - 1
        base = 131

        weights = [1] * width
        for i in range(1, width):
            weights[i] = weights[i - 1] * base % MOD

        hashes = []
        for word in words:
            value = 0
            for ch in word:
                value = (value * base + ord(ch)) % MOD
            hashes.append(value)

        for position in range(width):
            weight = weights[width - 1 - position]
            seen = {}
            for index, word in enumerate(words):
                blanked = (hashes[index] - ord(word[position]) * weight) % MOD
                for other in seen.get(blanked, ()):
                    candidate = words[other]
                    if all(candidate[t] == word[t] for t in range(width) if t != position):
                        return True
                seen.setdefault(blanked, []).append(index)
        return False
