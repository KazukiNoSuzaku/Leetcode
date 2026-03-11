# Given a string queryIP, return "IPv4" if IP is a valid IPv4 address,
# "IPv6" if IP is a valid IPv6 address or "Neither" if IP is not a correct IP of any type.

# Author: Kaustav Ghosh

class Solution(object):
    def validIPAddress(self, queryIP):
        if '.' in queryIP:
            parts = queryIP.split('.')
            if len(parts) != 4:
                return 'Neither'
            for p in parts:
                if not p or len(p) > 3 or (len(p) > 1 and p[0] == '0'):
                    return 'Neither'
                if not p.isdigit() or not (0 <= int(p) <= 255):
                    return 'Neither'
            return 'IPv4'
        elif ':' in queryIP:
            parts = queryIP.split(':')
            if len(parts) != 8:
                return 'Neither'
            hex_chars = set('0123456789abcdefABCDEF')
            for p in parts:
                if not p or len(p) > 4 or not all(c in hex_chars for c in p):
                    return 'Neither'
            return 'IPv6'
        return 'Neither'
