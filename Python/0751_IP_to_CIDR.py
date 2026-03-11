# Given an IP address and range n, return minimal list of CIDR blocks covering n IPs from that IP.

# Author: Kaustav Ghosh

class Solution(object):
    def ipToCIDR(self, ip, n):
        def ip_to_int(ip):
            parts = ip.split('.')
            return sum(int(p) << (24 - 8*i) for i, p in enumerate(parts))
        def int_to_ip(num):
            return '.'.join(str((num >> (24 - 8*i)) & 255) for i in range(4))
        start = ip_to_int(ip)
        res = []
        while n > 0:
            lowbit = start & (-start) or (1 << 32)
            k = 0
            tmp = lowbit
            while tmp > 1: tmp >>= 1; k += 1
            while (1 << k) > n: k -= 1
            res.append('%s/%d' % (int_to_ip(start), 32 - k))
            start += (1 << k)
            n -= (1 << k)
        return res
