# A string such as "word" contains abbreviations like "4", "w3d", "wo2", "wor1", "word".
# Given a target string and a set of strings in a dictionary, find an abbreviation of this
# target string with the smallest possible length such that it does not conflict with
# abbreviations of the strings in the dictionary.

# Author: Kaustav Ghosh

class Solution(object):
    def minAbbreviation(self, target, dictionary):
        n = len(target)
        if not dictionary:
            return str(n)

        # diff[i] = bitmask of positions where target differs from dictionary[i]
        diffs = []
        for word in dictionary:
            if len(word) != n:
                continue
            mask = 0
            for j in range(n):
                if target[j] != word[j]:
                    mask |= 1 << j
            diffs.append(mask)

        if not diffs:
            return str(n)

        def abbr_len(mask):
            # count length of abbreviation with 1-bits = keep, 0-bits = abbreviate
            length = 0
            prev_zero = False
            for j in range(n):
                if mask & (1 << j):
                    length += 1
                    prev_zero = False
                else:
                    if not prev_zero:
                        length += 1
                    prev_zero = True
            return length

        best = target  # worst case keep all chars
        for mask in range(1 << n):
            # mask bit=1 means keep that char
            if all(mask & diff for diff in diffs):
                # valid: differs from every dict word at at least one kept position
                ab = abbr_len(mask)
                if ab < len(best):
                    # build abbreviation string
                    res = []
                    count = 0
                    for j in range(n):
                        if mask & (1 << j):
                            if count:
                                res.append(str(count))
                                count = 0
                            res.append(target[j])
                        else:
                            count += 1
                    if count:
                        res.append(str(count))
                    best = ''.join(res)
        return best
