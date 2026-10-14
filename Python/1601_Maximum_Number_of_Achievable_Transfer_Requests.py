# Author: Kaustav Ghosh
# Problem: Maximum Number of Achievable Transfer Requests
# Approach: A set of requests is achievable exactly when every building ends with the same headcount it started with, which is a condition on the chosen subset alone and not on any ordering, so with at most sixteen requests I can simply search all subsets. Rather than recomputing the balance at each leaf I carry it along, adjusting two buildings per decision and keeping a count of how many buildings are currently off balance, so a leaf is accepted in constant time; a bound that gives up when even taking every remaining request could not beat the best found prunes most of the tree.

class Solution(object):
    def maximumRequests(self, n, requests):
        """
        :type n: int
        :type requests: List[List[int]]
        :rtype: int
        """
        total = len(requests)
        balance = [0] * n
        self.best = 0

        def search(index, taken, off_balance):
            if index == total:
                if off_balance == 0 and taken > self.best:
                    self.best = taken
                return
            if taken + (total - index) <= self.best:
                return
            # Skip this request.
            search(index + 1, taken, off_balance)
            # Take it: one building loses a person, another gains one.
            source, target = requests[index]
            if balance[source] == 0:
                off_balance += 1
            balance[source] -= 1
            if balance[source] == 0:
                off_balance -= 1
            if balance[target] == 0:
                off_balance += 1
            balance[target] += 1
            if balance[target] == 0:
                off_balance -= 1
            search(index + 1, taken + 1, off_balance)
            balance[source] += 1
            balance[target] -= 1

        search(0, 0, 0)
        return self.best
