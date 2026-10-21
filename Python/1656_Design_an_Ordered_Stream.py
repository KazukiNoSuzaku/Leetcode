# Author: Kaustav Ghosh
# Problem: Design an Ordered Stream
# Approach: Since exactly one insertion arrives per id and the chunks must concatenate into the full sorted order, every value is emitted exactly once and always in id order, so the whole state is a slot array plus a pointer at the lowest id not yet emitted. An insertion writes its slot and then, only if it filled the pointer's slot, walks the pointer forward over whatever is now contiguous; otherwise it returns an empty chunk. The pointer never moves backwards, so the total work across all n insertions is linear rather than a scan per call.

class OrderedStream(object):

    def __init__(self, n):
        """
        :type n: int
        """
        # One extra slot so the pointer can run off the end harmlessly.
        self.slots = [None] * (n + 2)
        self.pointer = 1

    def insert(self, idKey, value):
        """
        :type idKey: int
        :type value: str
        :rtype: List[str]
        """
        self.slots[idKey] = value
        chunk = []
        while self.slots[self.pointer] is not None:
            chunk.append(self.slots[self.pointer])
            self.pointer += 1
        return chunk


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
