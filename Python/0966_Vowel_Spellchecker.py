# Given a wordlist and queries, for each query return:
# exact match, or case-insensitive match, or vowel-error match, else "".

# Author: Kaustav Ghosh

class Solution(object):
    def spellchecker(self, wordlist, queries):
        word_set = set(wordlist)
        lower_map = {}
        vowel_map = {}
        import re
        def devowel(w):
            return re.sub('[aeiou]', '*', w.lower())
        for w in wordlist:
            lw = w.lower()
            if lw not in lower_map:
                lower_map[lw] = w
            dv = devowel(w)
            if dv not in vowel_map:
                vowel_map[dv] = w
        res = []
        for q in queries:
            if q in word_set:
                res.append(q)
            elif q.lower() in lower_map:
                res.append(lower_map[q.lower()])
            elif devowel(q) in vowel_map:
                res.append(vowel_map[devowel(q)])
            else:
                res.append('')
        return res
