# Author: Kaustav Ghosh
# 1114. Print in Order
# https://leetcode.com/problems/print-in-order/

import threading

class Foo(object):
    def __init__(self):
        self.event1 = threading.Event()
        self.event2 = threading.Event()

    def first(self, printFirst):
        """
        :type printFirst: method
        :rtype: void
        """
        printFirst()
        self.event1.set()

    def second(self, printSecond):
        """
        :type printSecond: method
        :rtype: void
        """
        self.event1.wait()
        printSecond()
        self.event2.set()

    def third(self, printThird):
        """
        :type printThird: method
        :rtype: void
        """
        self.event2.wait()
        printThird()
