class Solution:
    def sumPrefixScores(self, words: list[str]) -> list[int]:
        trie = {}
        for word in words:
            node = trie
            for ch in word:
                if ch not in node:
                    node[ch] = {'#': 0}
                node = node[ch]
                node['#'] += 1

        ans = []
        for word in words:
            node = trie
            score = 0
            for ch in word:
                node = node[ch]
                score += node['#']
            ans.append(score)
        return ans
