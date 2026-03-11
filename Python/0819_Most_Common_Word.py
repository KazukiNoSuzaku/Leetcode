# Find the most frequent word in a paragraph not in the banned list.

# Author: Kaustav Ghosh

import re
from collections import Counter

class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        banned_set = set(banned)
        words = re.findall(r'[a-zA-Z]+', paragraph.lower())
        count = Counter(w for w in words if w not in banned_set)
        return count.most_common(1)[0][0]
