from typing import List

class Solution:
    def canMakePalindromeQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        n = len(s) // 2

        # Prefix counts: left_pre[c][i] = occurrences of char c in s[0..i-1]
        # right_pre[c][i] = occurrences of s[2n-1-j] for j in [0..i-1]
        #                  = occurrences in s[n..2n-1] read right-to-left, i.e. s[l2..r2]
        left_pre = [[0] * (n + 1) for _ in range(26)]
        right_pre = [[0] * (n + 1) for _ in range(26)]
        bad_pre = [0] * (n + 1)  # bad_pre[i+1] = mismatches in pairs [0..i]

        for i in range(n):
            cl = ord(s[i]) - 97
            cr = ord(s[2 * n - 1 - i]) - 97
            for c in range(26):
                left_pre[c][i + 1] = left_pre[c][i]
                right_pre[c][i + 1] = right_pre[c][i]
            left_pre[cl][i + 1] += 1
            right_pre[cr][i + 1] += 1
            bad_pre[i + 1] = bad_pre[i] + (0 if cl == cr else 1)

        def lc(c, l, r):
            return left_pre[c][r + 1] - left_pre[c][l] if l <= r else 0

        def rc(c, l, r):
            return right_pre[c][r + 1] - right_pre[c][l] if l <= r else 0

        def bad(l, r):
            return bad_pre[r + 1] - bad_pre[l] if l <= r else 0

        res = []
        for l1, r1, l2, r2 in queries:
            # Map right range [l2,r2] to left-half mirror indices [l2m, r2m]
            l2m = 2 * n - 1 - r2
            r2m = 2 * n - 1 - l2

            # Overlap of [l1,r1] and [l2m,r2m]
            il = max(l1, l2m)
            ir = min(r1, r2m)
            ov = il <= ir

            # Pairs outside both ranges must already match
            bad_union = bad(l1, r1) + bad(l2m, r2m) - (bad(il, ir) if ov else 0)
            if bad_pre[n] - bad_union > 0:
                res.append(False)
                continue

            ok = True
            for c in range(26):
                lt = lc(c, l1, r1)   # left chars available in [l1,r1]
                rt = rc(c, l2m, r2m) # right chars available (= chars in s[l2..r2])

                # B region: [l1,r1] \ [l2m,r2m] — right side fixed, needs chars from left pool
                rnb = rc(c, l1, r1) - (rc(c, il, ir) if ov else 0)
                # C region: [l2m,r2m] \ [l1,r1] — left side fixed, needs chars from right pool
                lnc = lc(c, l2m, r2m) - (lc(c, il, ir) if ov else 0)

                if lt < rnb or rt < lnc or (lt - rnb) != (rt - lnc):
                    ok = False
                    break

            res.append(ok)

        return res
