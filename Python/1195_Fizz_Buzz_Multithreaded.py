# Author: Kaustav Ghosh
# Four threads with semaphores for fizz, buzz, fizzbuzz, and number

import threading

class FizzBuzz(object):
    def __init__(self, n):
        """
        :type n: int
        """
        self.n = n
        self.sem_fizz = threading.Semaphore(0)
        self.sem_buzz = threading.Semaphore(0)
        self.sem_fizzbuzz = threading.Semaphore(0)
        self.sem_number = threading.Semaphore(1)
        self.current = 1

    def fizz(self, printFizz):
        while True:
            self.sem_fizz.acquire()
            if self.current > self.n:
                return
            printFizz()
            self.current += 1
            self._release_next()

    def buzz(self, printBuzz):
        while True:
            self.sem_buzz.acquire()
            if self.current > self.n:
                return
            printBuzz()
            self.current += 1
            self._release_next()

    def fizzbuzz(self, printFizzBuzz):
        while True:
            self.sem_fizzbuzz.acquire()
            if self.current > self.n:
                return
            printFizzBuzz()
            self.current += 1
            self._release_next()

    def number(self, printNumber):
        while True:
            self.sem_number.acquire()
            if self.current > self.n:
                self.sem_fizz.release()
                self.sem_buzz.release()
                self.sem_fizzbuzz.release()
                return
            printNumber(self.current)
            self.current += 1
            self._release_next()

    def _release_next(self):
        i = self.current
        if i > self.n:
            self.sem_fizz.release()
            self.sem_buzz.release()
            self.sem_fizzbuzz.release()
            self.sem_number.release()
        elif i % 15 == 0:
            self.sem_fizzbuzz.release()
        elif i % 3 == 0:
            self.sem_fizz.release()
        elif i % 5 == 0:
            self.sem_buzz.release()
        else:
            self.sem_number.release()
