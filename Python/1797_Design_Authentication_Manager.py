# Author: Kaustav Ghosh
# Problem: Design Authentication Manager
# Approach: The call times are promised to be strictly increasing, and every generate or renew sets the expiry to that time plus a fixed lifetime, so expiries are handed out in increasing order too. Keeping the tokens in an ordered mapping and moving a token to the back whenever it is refreshed therefore keeps the whole structure sorted by expiry for free, which means expired tokens are always a prefix. Each call drops that prefix from the front, so counting is just the size of the mapping and every token is removed exactly once over the lifetime of the manager instead of the table being rescanned on every count.

class AuthenticationManager(object):

    def __init__(self, timeToLive):
        """
        :type timeToLive: int
        """
        from collections import OrderedDict

        self.lifetime = timeToLive
        self.expiry = OrderedDict()

    def _discardExpired(self, currentTime):
        while self.expiry:
            tokenId, expires = next(iter(self.expiry.items()))
            if expires > currentTime:
                break
            self.expiry.popitem(last=False)

    def generate(self, tokenId, currentTime):
        """
        :type tokenId: str
        :type currentTime: int
        :rtype: None
        """
        self._discardExpired(currentTime)
        self.expiry[tokenId] = currentTime + self.lifetime
        self.expiry.move_to_end(tokenId)

    def renew(self, tokenId, currentTime):
        """
        :type tokenId: str
        :type currentTime: int
        :rtype: None
        """
        self._discardExpired(currentTime)
        if tokenId in self.expiry:
            self.expiry[tokenId] = currentTime + self.lifetime
            self.expiry.move_to_end(tokenId)

    def countUnexpiredTokens(self, currentTime):
        """
        :type currentTime: int
        :rtype: int
        """
        self._discardExpired(currentTime)
        return len(self.expiry)


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)
