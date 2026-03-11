# Given a rows x cols screen and a sentence represented as a list of strings,
# return the number of times the given sentence can be fitted on the screen.

# Author: Kaustav Ghosh

class Solution(object):
    def wordsTyping(self, sentence, rows, cols):
        s = ' '.join(sentence) + ' '
        n = len(s)
        start = 0
        for _ in range(rows):
            start += cols
            if s[start % n] == ' ':
                start += 1
            else:
                while start > 0 and s[(start - 1) % n] != ' ':
                    start -= 1
        return start // n
