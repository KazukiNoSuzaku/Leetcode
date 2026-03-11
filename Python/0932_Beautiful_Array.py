# Construct a beautiful array of size n (no A[k]*2 == A[i]+A[j] for i<k<j).

# Author: Kaustav Ghosh

class Solution(object):
    def beautifulArray(self, n):
        memo = {1: [1]}
        def f(n):
            if n in memo: return memo[n]
            odd = f((n+1)//2)
            even = f(n//2)
            memo[n] = [2*x-1 for x in odd] + [2*x for x in even]
            return memo[n]
        return f(n)
