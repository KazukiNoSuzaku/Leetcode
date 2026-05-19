from sortedcontainers import SortedList

class Solution:
    def beautifulPair(self, nums1: list[int], nums2: list[int]) -> list[int]:
        n = len(nums1)
        # Transform to Chebyshev: L1(i,j) = max(|ui-uj|, |vi-vj|), u=x+y, v=x-y
        order = sorted(range(n), key=lambda i: (nums1[i] + nums2[i], nums1[i] - nums2[i], i))

        best_d = float('inf')
        best_pair = (n, n)
        sl = SortedList()  # stores (v, index) sorted naturally
        left = 0

        for r in range(n):
            ir = order[r]
            ur = nums1[ir] + nums2[ir]
            vr = nums1[ir] - nums2[ir]

            while left < r:
                il = order[left]
                if ur - (nums1[il] + nums2[il]) > best_d:
                    sl.remove((nums1[il] - nums2[il], il))
                    left += 1
                else:
                    break

            lo_idx = sl.bisect_left((vr - best_d, -1))
            while lo_idx < len(sl) and sl[lo_idx][0] <= vr + best_d:
                vj, ij = sl[lo_idx]
                d = abs(nums1[ir] - nums1[ij]) + abs(nums2[ir] - nums2[ij])
                pair = (min(ir, ij), max(ir, ij))
                if d < best_d or (d == best_d and pair < best_pair):
                    best_d = d
                    best_pair = pair
                lo_idx += 1

            sl.add((vr, ir))

        return list(best_pair)
