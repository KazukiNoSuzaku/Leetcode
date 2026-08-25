# Author: Kaustav Ghosh
# Problem: Count Words Obtained After Adding a Letter
# Approach: All words have distinct letters, so represent each as a 26-bit mask. A target is reachable if removing exactly one of its letters yields a start word's mask. Store start masks in a set and probe each target by clearing one bit at a time

class Solution(object):
    def wordCount(self, startWords, targetWords):
        """
        :type startWords: List[str]
        :type targetWords: List[str]
        :rtype: int
        """
        def mask(word):
            m = 0
            for ch in word:
                m |= 1 << (ord(ch) - 97)
            return m

        start_masks = {mask(w) for w in startWords}
        count = 0
        for t in targetWords:
            tmask = mask(t)
            for ch in t:
                if (tmask ^ (1 << (ord(ch) - 97))) in start_masks:
                    count += 1
                    break
        return count
