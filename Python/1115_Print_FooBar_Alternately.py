# Author: Kaustav Ghosh
# 1115. Print FooBar Alternately
# https://leetcode.com/problems/print-foobar-alternately/

import threading

class FooBar(object):
    def __init__(self, n):
        self.n = n
        self.foo_sem = threading.Semaphore(1)
        self.bar_sem = threading.Semaphore(0)

    def foo(self, printFoo):
        """
        :type printFoo: method
        :rtype: void
        """
        for _ in range(self.n):
            self.foo_sem.acquire()
            printFoo()
            self.bar_sem.release()

    def bar(self, printBar):
        """
        :type printBar: method
        :rtype: void
        """
        for _ in range(self.n):
            self.bar_sem.acquire()
            printBar()
            self.foo_sem.release()
