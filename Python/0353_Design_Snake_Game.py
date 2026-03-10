# Design a Snake game that is played on a device with screen size height x width.
# The snake is initially positioned at the top left corner (0, 0) with a length of 1 unit.
# You are given an array food where food[i] = (ri, ci) is the row and column position of
# a piece of food that the snake can eat. When the snake eats a piece of food, its length
# and the game's score both increase by 1.
# Return the game's score after applying the direction command; -1 if the game is over.

# Constraints:
# 1 <= width, height <= 10^4
# 1 <= food.length <= 50

# Author: Kaustav Ghosh

from collections import deque

class SnakeGame(object):
    def __init__(self, width, height, food):
        self.width = width
        self.height = height
        self.food = deque(food)
        self.snake = deque([(0, 0)])
        self.snake_set = {(0, 0)}
        self.score = 0

    def move(self, direction):
        r, c = self.snake[0]
        dr = {'U': -1, 'D': 1, 'L': 0, 'R': 0}
        dc = {'U': 0, 'D': 0, 'L': -1, 'R': 1}
        nr, nc = r + dr[direction], c + dc[direction]
        if nr < 0 or nr >= self.height or nc < 0 or nc >= self.width:
            return -1
        tail = self.snake[-1]
        self.snake_set.discard(tail)
        if (nr, nc) in self.snake_set:
            return -1
        self.snake.appendleft((nr, nc))
        self.snake_set.add((nr, nc))
        if self.food and [nr, nc] == list(self.food[0]):
            self.food.popleft()
            self.score += 1
            self.snake_set.add(tail)
        else:
            self.snake.pop()
        return self.score
