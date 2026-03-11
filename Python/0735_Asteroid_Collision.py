# Simulate asteroid collisions: positive moves right, negative moves left.

# Author: Kaustav Ghosh

class Solution(object):
    def asteroidCollision(self, asteroids):
        stack = []
        for a in asteroids:
            while stack and a < 0 < stack[-1]:
                if stack[-1] < -a:
                    stack.pop(); continue
                elif stack[-1] == -a:
                    stack.pop()
                break
            else:
                stack.append(a)
        return stack
