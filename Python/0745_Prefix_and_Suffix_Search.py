# Design a WordFilter with f(prefix, suffix) returning highest weight word index.

# Author: Kaustav Ghosh

class WordFilter(object):
    def __init__(self, words):
        self.lookup = {}
        for i, word in enumerate(words):
            n = len(word)
            for p in range(n + 1):
                for s in range(n + 1):
                    key = word[:p] + '#' + word[s:]
                    self.lookup[key] = i

    def f(self, pref, suff):
        return self.lookup.get(pref + '#' + suff, -1)
