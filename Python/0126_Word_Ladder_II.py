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

from collections import defaultdict, deque

class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        word_set = set(wordList)
        if endWord not in word_set:
            return []

        layer = {beginWord: [[beginWord]]}
        while layer:
            word_set -= set(layer.keys())
            next_layer = defaultdict(list)
            for word, paths in layer.items():
                for i in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        next_word = word[:i] + c + word[i+1:]
                        if next_word in word_set:
                            next_layer[next_word] += [path + [next_word] for path in paths]
            if endWord in next_layer:
                return next_layer[endWord]
            layer = next_layer
        return []
