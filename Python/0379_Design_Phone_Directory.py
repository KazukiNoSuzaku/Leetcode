# Design a phone directory which manages a phone number pool. The phone number pool
# has maxNumbers of phone numbers (0 to maxNumbers - 1).
# Implement the PhoneDirectory class:
# - get() Provide a number which is not assigned to anyone. Return -1 if none available.
# - check(number) Return if the number is available or not.
# - release(number) Recycle or release a number.

# Constraints:
# 1 <= maxNumbers <= 10^4
# 0 <= number < maxNumbers
# At most 2 * 10^4 calls will be made to get, check, and release.

# Author: Kaustav Ghosh

class PhoneDirectory(object):
    def __init__(self, maxNumbers):
        self.available = set(range(maxNumbers))

    def get(self):
        if not self.available:
            return -1
        return self.available.pop()

    def check(self, number):
        return number in self.available

    def release(self, number):
        self.available.add(number)
