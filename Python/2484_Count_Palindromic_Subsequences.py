class Solution:
    def countPalindromes(self, s: str) -> int:
        MOD = 10 ** 9 + 7
        n = len(s)

        # A length-5 palindrome has the form s[i] s[j] s[k] s[l] s[m] where
        # s[i]==s[m] and s[j]==s[l]. For each center k, count prefix pairs
        # (a,b) with i<j<k and suffix pairs (b,a) with k<l<m.
        # Answer = sum_k sum_{a,b} pre_pairs[a][b] * suf_pairs[b][a].

        # Build suffix pair counts (all positions initially, then remove as we scan left-to-right)
        suf_pairs = [[0] * 26 for _ in range(26)]
        suf_cnt = [0] * 26
        for i in range(n - 1, -1, -1):
            c = ord(s[i]) - ord('a')
            for b in range(26):
                suf_pairs[c][b] += suf_cnt[b]
            suf_cnt[c] += 1

        pre_pairs = [[0] * 26 for _ in range(26)]
        pre_cnt = [0] * 26
        ans = 0

        for k in range(n):
            c = ord(s[k]) - ord('a')
            # Remove position k from suffix (pairs starting at k)
            for b in range(26):
                suf_pairs[c][b] -= suf_cnt[b]
            suf_pairs[c][c] += 1  # fix over-subtraction when b == c
            suf_cnt[c] -= 1

            # Accumulate palindromes centered at k
            for a in range(26):
                for b in range(26):
                    ans = (ans + pre_pairs[a][b] * suf_pairs[b][a]) % MOD

            # Add position k to prefix
            for a in range(26):
                pre_pairs[a][c] += pre_cnt[a]
            pre_cnt[c] += 1

        return ans
