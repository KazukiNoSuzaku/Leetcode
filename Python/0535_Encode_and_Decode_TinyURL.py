# TinyURL is a URL shortening service. Implement encode and decode functions.

# Author: Kaustav Ghosh

class Codec:
    def __init__(self):
        self.url_to_code = {}
        self.code_to_url = {}
        self.base = 'http://tinyurl.com/'

    def encode(self, longUrl):
        if longUrl not in self.url_to_code:
            code = str(len(self.url_to_code) + 1)
            self.url_to_code[longUrl] = code
            self.code_to_url[code] = longUrl
        return self.base + self.url_to_code[longUrl]

    def decode(self, shortUrl):
        return self.code_to_url[shortUrl[len(self.base):]]
