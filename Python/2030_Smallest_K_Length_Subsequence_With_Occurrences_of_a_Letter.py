# Author: Kaustav Ghosh
# Problem 2030: Smallest K-Length Subsequence With Occurrences of a Letter

class Solution(object):
    def smallestSubsequence(self, s, k, letter, repetition):
        """
        :type s: str
        :type k: int
        :type letter: str
        :type repetition: int
        :rtype: str
        """
        n = len(s)
        # Count remaining occurrences of letter from each position
        suffix_letter = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_letter[i] = suffix_letter[i + 1] + (1 if s[i] == letter else 0)

        stack = []
        letter_in_stack = 0

        for i in range(n):
            while stack and stack[-1] > s[i]:
                # Can we pop? Check constraints
                remaining = n - i  # chars left including current
                if len(stack) - 1 + remaining < k:
                    break
                if stack[-1] == letter:
                    if letter_in_stack - 1 + suffix_letter[i] < repetition:
                        break
                    letter_in_stack -= 1
                stack.pop()

            if len(stack) < k:
                if s[i] == letter:
                    stack.append(s[i])
                    letter_in_stack += 1
                else:
                    # Only add non-letter if we can still fit enough letters
                    remaining_spots = k - len(stack) - 1
                    remaining_letters = suffix_letter[i + 1]
                    needed = repetition - letter_in_stack
                    if remaining_spots >= needed:
                        stack.append(s[i])
                    elif remaining_letters >= needed:
                        # Skip this char
                        pass

        return ''.join(stack)
