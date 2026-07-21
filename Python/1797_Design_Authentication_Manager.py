# Author: Kaustav Ghosh
# Problem: Design Authentication Manager
# Approach: Store each token's expiry time; renew only if the token is still unexpired, and count how many expiries are strictly in the future

class AuthenticationManager(object):
    def __init__(self, timeToLive):
        """
        :type timeToLive: int
        """
        self.ttl = timeToLive
        self.expiry = {}

    def generate(self, tokenId, currentTime):
        """
        :type tokenId: str
        :type currentTime: int
        :rtype: None
        """
        self.expiry[tokenId] = currentTime + self.ttl

    def renew(self, tokenId, currentTime):
        """
        :type tokenId: str
        :type currentTime: int
        :rtype: None
        """
        if self.expiry.get(tokenId, 0) > currentTime:
            self.expiry[tokenId] = currentTime + self.ttl

    def countUnexpiredTokens(self, currentTime):
        """
        :type currentTime: int
        :rtype: int
        """
        return sum(1 for exp in self.expiry.values() if exp > currentTime)
