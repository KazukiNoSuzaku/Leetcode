# A transformation sequence from word beginWord to word endWord using a dictionary wordList
# is a sequence beginWord -> s1 -> s2 -> ... -> sk such that:
# - Every adjacent pair of words differs by a single letter.
# - Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
# - sk == endWord
# Given two words, beginWord and endWord, and a word dictionary wordList, return all the
# shortest transformation sequences from beginWord to endWord.

# Example 1:
# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
# Output: [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]

# Example 2:
# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
# Output: []

# Constraints:
# 1 <= beginWord.length <= 5
# endWord.length == beginWord.length
# 1 <= wordList.length <= 500
# wordList[i].length == beginWord.length
# All words consist of lowercase English letters.

# Author: Kaustav Ghosh

from collections import defaultdict

class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        word_set = set(wordList)
        if endWord not in word_set:
            return []

        # BFS: build parent graph (only store edges, not full paths)
        parents = defaultdict(set)
        current_level = {beginWord}
        visited = {beginWord}
        found = False

        while current_level and not found:
            next_level = set()
            for word in current_level:
                for i in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        nw = word[:i] + c + word[i+1:]
                        if nw in word_set and nw not in visited:
                            next_level.add(nw)
                            parents[nw].add(word)
                            if nw == endWord:
                                found = True
            visited |= next_level
            current_level = next_level

        if not found:
            return []

        # DFS: reconstruct all shortest paths from parent graph
        result = []
        def dfs(word, path):
            if word == beginWord:
                result.append(path[::-1])
                return
            for parent in parents[word]:
                path.append(parent)
                dfs(parent, path)
                path.pop()

        dfs(endWord, [endWord])
        return result
