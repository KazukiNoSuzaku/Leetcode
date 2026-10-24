# Author: Kaustav Ghosh
# Problem: Number of Distinct Substrings in a String
# Approach: Collecting every slice into a set costs cubic time and quadratic memory, so instead I build a suffix automaton, the smallest automaton recognising exactly the substrings of the string, which answers the follow-up's request for linear time. Each of its states stands for a group of substrings sharing the same set of end positions, and the lengths within a state form a contiguous run bounded below by its suffix link, so the number of distinct substrings is the sum over states of its own longest length minus that of its link. The construction extends the automaton one character at a time, redirecting transitions along the suffix chain and splitting a state into a clone whenever an existing transition is reached by a longer route than it represents.

class Solution(object):
    def countDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = [0]
        link = [-1]
        transitions = [{}]
        last = 0

        for ch in s:
            current = len(length)
            length.append(length[last] + 1)
            link.append(-1)
            transitions.append({})

            walker = last
            while walker != -1 and ch not in transitions[walker]:
                transitions[walker][ch] = current
                walker = link[walker]

            if walker == -1:
                link[current] = 0
            else:
                existing = transitions[walker][ch]
                if length[walker] + 1 == length[existing]:
                    link[current] = existing
                else:
                    # Split: the existing state is reached by a longer path than it covers.
                    clone = len(length)
                    length.append(length[walker] + 1)
                    link.append(link[existing])
                    transitions.append(dict(transitions[existing]))
                    while walker != -1 and transitions[walker].get(ch) == existing:
                        transitions[walker][ch] = clone
                        walker = link[walker]
                    link[existing] = clone
                    link[current] = clone
            last = current

        return sum(length[state] - length[link[state]] for state in range(1, len(length)))
