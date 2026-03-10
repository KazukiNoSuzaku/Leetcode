# Design a logger system that receives a stream of messages along with their timestamps.
# Each unique message should only be printed at most every 10 seconds
# (i.e. a message printed at timestamp t will prevent other identical messages from
# being printed until timestamp t + 10).
# All messages will come in chronological order.

# Example 1:
# Input: ["Logger", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage",
#         "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage"]
#        [[], [1, "foo"], [2, "bar"], [3, "foo"], [8, "bar"], [10, "foo"], [11, "foo"]]
# Output: [null, true, true, false, false, false, true]

# Constraints:
# 0 <= timestamp <= 10^9
# Every timestamp will be passed in non-decreasing order (chronological order).
# 1 <= message.length <= 30
# At most 10^4 calls will be made to shouldPrintMessage.

# Author: Kaustav Ghosh

class Logger(object):
    def __init__(self):
        self.last_printed = {}

    def shouldPrintMessage(self, timestamp, message):
        if message not in self.last_printed or timestamp - self.last_printed[message] >= 10:
            self.last_printed[message] = timestamp
            return True
        return False
