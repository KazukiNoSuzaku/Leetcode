# Mask an email or phone number according to specified rules.

# Author: Kaustav Ghosh

class Solution(object):
    def maskPII(self, s):
        if '@' in s:
            s = s.lower()
            name, domain = s.split('@')
            return name[0] + '*****' + name[-1] + '@' + domain
        else:
            digits = ''.join(c for c in s if c.isdigit())
            masked = '***-***-' + digits[-4:]
            if len(digits) == 11: return '+*-' + masked
            if len(digits) == 12: return '+**-' + masked
            if len(digits) == 13: return '+***-' + masked
            return masked
