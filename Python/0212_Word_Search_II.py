# Given an m x n board of characters and a list of strings words,
# return all words on the board. Each word must be constructed from letters of sequentially
# adjacent cells (horizontally or vertically neighboring). The same cell may not be used more
# than once in a word.

# Example 1:
# Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],
#        words = ["oath","pea","eat","rain"]
# Output: ["eat","oath"]

# Constraints:
# m == board.length, n == board[i].length
# 1 <= m, n <= 12
# 1 <= words.length <= 3 * 10^4
# 1 <= words[i].length <= 10

# Author: Kaustav Ghosh

class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.word = None

class Solution(object):
    def findWords(self, board, words):
        root = TrieNode()
        for word in words:
            node = root
            for c in word:
                if c not in node.children:
                    node.children[c] = TrieNode()
                node = node.children[c]
            node.word = word

        m, n = len(board), len(board[0])
        result = []

        def dfs(node, r, c):
            c_val = board[r][c]
            if c_val not in node.children:
                return
            next_node = node.children[c_val]
            if next_node.word:
                result.append(next_node.word)
                next_node.word = None
            board[r][c] = '#'
            for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] != '#':
                    dfs(next_node, nr, nc)
            board[r][c] = c_val

        for r in range(m):
            for c in range(n):
                dfs(root, r, c)
        return result
