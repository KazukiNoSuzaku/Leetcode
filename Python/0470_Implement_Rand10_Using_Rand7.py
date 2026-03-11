# Given the API rand7() that generates a uniform random integer in the range [1, 7],
# write a function rand10() that generates a uniform random integer in the range [1, 10].
# You can only call the API rand7(), and you shouldn't call any other API.

# Author: Kaustav Ghosh

class Solution(object):
    def rand10(self):
        while True:
            row = rand7()
            col = rand7()
            idx = (row - 1) * 7 + col  # uniform in [1, 49]
            if idx <= 40:
                return (idx - 1) % 10 + 1
