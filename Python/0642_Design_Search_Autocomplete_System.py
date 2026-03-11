# Design a search autocomplete system returning top 3 hot queries for each character typed.

# Author: Kaustav Ghosh

from collections import defaultdict

class AutocompleteSystem(object):
    def __init__(self, sentences, times):
        self.counts = defaultdict(int)
        for s, t in zip(sentences, times):
            self.counts[s] = t
        self.cur = ''

    def input(self, c):
        if c == '#':
            self.counts[self.cur] += 1
            self.cur = ''
            return []
        self.cur += c
        results = [(cnt, s) for s, cnt in self.counts.items() if s.startswith(self.cur)]
        results.sort(key=lambda x: (-x[0], x[1]))
        return [s for _, s in results[:3]]
