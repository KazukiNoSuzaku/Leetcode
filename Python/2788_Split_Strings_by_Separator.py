class Solution:
    def splitWordsBySeparator(self, words: list[str], separator: str) -> list[str]:
        return [part for w in words for part in w.split(separator) if part]
