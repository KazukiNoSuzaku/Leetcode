# Author: Kaustav Ghosh
# Problem: Encrypt and Decrypt Strings
# Approach: Encryption maps each character to its fixed length-2 value, so it is a direct substitution. Decryption is ambiguous, but the count of dictionary words that decrypt to a target equals the number of dictionary words whose encryption is that target. Precompute a Counter of encryptions of all dictionary words; decrypt is then a single lookup

from collections import Counter


class Encrypter(object):
    def __init__(self, keys, values, dictionary):
        """
        :type keys: List[str]
        :type values: List[str]
        :type dictionary: List[str]
        """
        self.key2val = {k: v for k, v in zip(keys, values)}
        self.enc_count = Counter()
        for word in dictionary:
            enc = self.encrypt(word)
            if enc:  # only words fully encryptable can ever match
                self.enc_count[enc] += 1

    def encrypt(self, word1):
        """
        :type word1: str
        :rtype: str
        """
        parts = []
        for ch in word1:
            if ch not in self.key2val:
                return ""
            parts.append(self.key2val[ch])
        return "".join(parts)

    def decrypt(self, word2):
        """
        :type word2: str
        :rtype: int
        """
        return self.enc_count[word2]
