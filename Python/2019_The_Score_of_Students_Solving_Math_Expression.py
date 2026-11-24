# Author: Kaustav Ghosh
# Problem: The Score of Students Solving Math Expression
# Approach: The true answer follows the usual precedence and is computed directly, while a student's wrong answer earns partial credit only if it can be produced by applying the two operators in some other order, which is exactly the set of values reachable by some bracketing. That set is built up over intervals of the expression: an interval's reachable values come from splitting it at each operator and combining every value of the left part with every value of the right part. Values above the largest possible answer are dropped to keep the sets small, but dropping them outright would be wrong, because a huge value multiplied by a zero collapses back to zero, so each interval also carries a flag recording that it can exceed the cap and that flag is allowed to contribute a zero through a multiplication.

class Solution(object):
    def scoreOfStudents(self, s, answers):
        """
        :type s: str
        :type answers: List[int]
        :rtype: int
        """
        LIMIT = 1000
        digits = [int(s[index]) for index in range(0, len(s), 2)]
        operators = [s[index] for index in range(1, len(s), 2)]
        count = len(digits)

        correct = 0
        for term in s.split('+'):
            product = 1
            for factor in term.split('*'):
                product *= int(factor)
            correct += product

        small = [[set() for _ in range(count)] for _ in range(count)]
        oversized = [[False] * count for _ in range(count)]
        for index in range(count):
            small[index][index] = set([digits[index]])

        for width in range(2, count + 1):
            for left in range(count - width + 1):
                right = left + width - 1
                values = set()
                beyond = False
                for split in range(left, right):
                    operator = operators[split]
                    lower = small[left][split]
                    upper = small[split + 1][right]
                    lower_beyond = oversized[left][split]
                    upper_beyond = oversized[split + 1][right]
                    for first in lower:
                        for second in upper:
                            value = first + second if operator == '+' else first * second
                            if value <= LIMIT:
                                values.add(value)
                            else:
                                beyond = True
                    if operator == '+':
                        if lower_beyond or upper_beyond:
                            beyond = True
                    else:
                        if lower_beyond:
                            if 0 in upper:
                                values.add(0)
                            if upper_beyond or any(second != 0 for second in upper):
                                beyond = True
                        if upper_beyond:
                            if 0 in lower:
                                values.add(0)
                            if lower_beyond or any(first != 0 for first in lower):
                                beyond = True
                small[left][right] = values
                oversized[left][right] = beyond

        reachable = small[0][count - 1]
        score = 0
        for answer in answers:
            if answer == correct:
                score += 5
            elif answer in reachable:
                score += 2
        return score
