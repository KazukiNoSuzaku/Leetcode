# Reorder logs: letter logs sorted, then digit logs in original order.

# Author: Kaustav Ghosh

class Solution(object):
    def reorderLogFiles(self, logs):
        letter_logs = []
        digit_logs = []
        for log in logs:
            if log.split()[1].isdigit(): digit_logs.append(log)
            else: letter_logs.append(log)
        letter_logs.sort(key=lambda l: (l.split(None, 1)[1], l.split()[0]))
        return letter_logs + digit_logs
