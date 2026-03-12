# Premium problem - not available without subscription
# Author: Kaustav Ghosh
# Typical approach: Recursion to print linked list in reverse

class Solution(object):
    def printLinkedListInReverse(self, head):
        """
        :type head: ImmutableListNode
        :rtype: None
        """
        if head:
            self.printLinkedListInReverse(head.getNext())
            head.printValue()
