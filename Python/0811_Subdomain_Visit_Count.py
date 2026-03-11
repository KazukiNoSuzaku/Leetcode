# Count visits to each subdomain from a list of count-domain pairs.

# Author: Kaustav Ghosh

from collections import defaultdict

class Solution(object):
    def subdomainVisits(self, cpdomains):
        counts = defaultdict(int)
        for cp in cpdomains:
            cnt, domain = cp.split()
            cnt = int(cnt)
            parts = domain.split('.')
            for i in range(len(parts)):
                counts['.'.join(parts[i:])] += cnt
        return ['%d %s' % (v, k) for k, v in counts.items()]
