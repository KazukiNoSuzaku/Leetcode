# Author: Kaustav Ghosh

class AuthenticationManager(object):
    def __init__(self, timeToLive):
        """
        :type timeToLive: int
        """
        self.ttl = timeToLive
        self.tokens = {}

    def generate(self, tokenId, currentTime):
        """
        :type tokenId: str
        :type currentTime: int
        :rtype: None
        """
        self.tokens[tokenId] = currentTime + self.ttl

    def renew(self, tokenId, currentTime):
        """
        :type tokenId: str
        :type currentTime: int
        :rtype: None
        """
        if tokenId in self.tokens and self.tokens[tokenId] > currentTime:
            self.tokens[tokenId] = currentTime + self.ttl

    def countUnexpiredTokens(self, currentTime):
        """
        :type currentTime: int
        :rtype: int
        """
        return sum(1 for t in self.tokens.values() if t > currentTime)
