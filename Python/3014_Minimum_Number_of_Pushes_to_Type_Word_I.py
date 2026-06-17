class Solution:
    def minimumPushes(self, word: str) -> int:
        # word has distinct letters; n letters mapped to 8 keys
        # first 8 get 1 push, next 8 get 2 pushes, etc.
        return sum((i // 8) + 1 for i in range(len(word)))
