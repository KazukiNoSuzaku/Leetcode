# Author: Kaustav Ghosh
# https://leetcode.com/problems/the-earliest-and-latest-rounds-where-players-compete/

class Solution(object):
    def earliestAndLatest(self, n, firstPlayer, secondPlayer):
        """
        :type n: int
        :type firstPlayer: int
        :type secondPlayer: int
        :rtype: List[int]
        """
        from functools import lru_cache

        def solve(n, f, s):
            # f and s are 1-indexed positions, f < s
            if f + s == n + 1:
                return (1, 1)
            earliest = float('inf')
            latest = 0
            half = n // 2
            # Enumerate all possible outcomes
            # f stays in position min(f, ...) and s stays
            # After round, positions become based on winners
            # f is at position f, s is at position s in a line of n
            # Pairs: (1,n), (2,n-1), ...
            # f_pos and s_pos after this round
            if s <= half:
                # Both in first half
                for new_n_val in [half + (n % 2)]:
                    # f keeps position f, s keeps position s
                    e, l = solve(new_n_val, f, s)
                    earliest = min(earliest, e)
                    latest = max(latest, l)
            elif f > half:
                # Both in second half - mirror
                new_f = n + 1 - s
                new_s = n + 1 - f
                for new_n_val in [half + (n % 2)]:
                    e, l = solve(new_n_val, new_f, new_s)
                    earliest = min(earliest, e)
                    latest = max(latest, l)
            else:
                # f in first half, s in second half (or one is middle)
                # f < s, f <= half, s > half
                # f fights someone from second half (not s since f+s != n+1)
                # s fights someone from first half (not f)
                # After round: f can be at positions [1..f], s can be at positions depending
                nxt = half + (n % 2)
                for i in range(1, f + 1):
                    for j in range(i + 1, nxt + 1):
                        # Check if this (i, j) is achievable
                        # i = number of first-half winners before f's match + (f wins)
                        # We need: winners from first (f-1) pairs that are from first half: can be 0..min(f-1, half - something)
                        # This is complex; use a direct enumeration approach
                        pass
                # Use recursion with memoization on (n, f, s)
                pass

            return (earliest + 1, latest + 1)

        # Better approach: BFS/DFS with memoization
        memo = {}

        def dp(n, f, s):
            if (n, f, s) in memo:
                return memo[(n, f, s)]
            if f + s == n + 1:
                memo[(n, f, s)] = (1, 1)
                return (1, 1)
            half = n // 2
            mn, mx = float('inf'), 0
            nxt = (n + 1) // 2
            # Number of players before f: f-1, between f and s: s-f-1, after s: n-s
            # f is paired with n+1-f, s is paired with n+1-s
            # Both f and s win their matches
            # We need to figure out how many of the other matches' winners end up before f and between f and s
            bf = f - 1  # players before f
            mid = s - f - 1  # players between f and s
            af = n - s  # players after s
            # f's opponent is at position n+1-f (in second half since f+s!=n+1 means n+1-f != s)
            # s's opponent is at position n+1-s
            # Pairs that are entirely before f or their mirror is entirely after s
            # Let's enumerate: how many winners from the "before f" side end up before f
            # Positions 1..f-1 are paired with positions n+1-(f-1)..n (i.e., n-f+2..n)
            # These pairs each produce one winner; the winner goes to position based on their original half
            # If the first-half player wins, they keep their rank; if second-half, they take position of first-half
            # Actually the next round positions are just the sorted order of winners
            # Winners from positions 1..half go to positions 1..half (keeping order)
            # So # of winners before new_f = # of first-half winners among pairs involving positions < f
            # Let a = winners from pairs (1,n),(2,n-1),...,(f-1,n-f+2) that are from first half
            # Let b = winners from pairs (f+1,n-f),...,(s-1,n-s+2) where both are between f and s or mirrored
            # This is getting complex. Let me use a cleaner approach.

            # Pairs: (1,n), (2,n-1), ..., (half, half+1) if n even, middle player passes if n odd
            # f is at position f, paired with n+1-f
            # s is at position s, paired with n+1-s
            # Both f and s win.
            # For other pairs, either player can win.
            # After the round, all winners are re-ranked 1..nxt
            # new_f = 1 + (number of winners whose original position < f)
            # new_s = new_f + 1 + (number of winners whose original position is between f and s)

            # Group pairs:
            # Group A: both players < f (and > n+1-f), i.e., pairs (i, n+1-i) where i < f and n+1-i > s
            #          This means i < f and i < n+1-s, i.e., i < min(f, n+1-s)
            #          Since f < s, n+1-s < n+1-f. And n+1-s could be < f or >= f.
            #          If n+1-s < f, then pair (i, n+1-i) has i < n+1-s and n+1-i > s
            #          The winner is always < f (one is < f, other is > s, if first half wins -> < f)
            #          Actually no: if i < f and n+1-i > s, winner position depends on who wins
            #          If player i wins, new position counts i as before f. If player n+1-i wins, they are after s.

            # Let me just enumerate all possible (new_f, new_s) pairs
            # Count pairs before f: pairs (i, n+1-i) for i=1..f-1 where n+1-i > s (both outside f..s range)
            # These are i < f and n+1-i > s => i < n+1-s => i < min(f, n+1-s)
            a = min(f - 1, n - s)  # pairs where one is before f and other is after s
            # Pairs between f and s: pairs (i, n+1-i) for f < i < s and f < n+1-i < s
            # i.e., f < i and i < s and f < n+1-i and n+1-i < s
            # => f < i < s and n+1-s < i < n+1-f
            # => max(f, n+1-s) < i < min(s, n+1-f)
            lo_b = max(f, n + 1 - s)
            hi_b = min(s, n + 1 - f)
            b = max(0, (hi_b - lo_b - 1))  # integer pairs strictly between
            # Pairs crossing: one between f and s, other also between (but mirrored outside)
            # Remaining pairs have one player between f and s and the other outside
            # c = pairs where one is between f and s, other is before f or after s
            c = (s - f - 1 - b * 2) // 2 if s - f - 1 > 2 * b else 0
            # Actually let me simplify: just enumerate possible values of new_f and new_s
            # For each pair in group A, if first-half wins: contributes to "before f" count
            # For each pair in group crossing, winner could be before f or between f and s
            # This is too complex for inline. Let me use a simpler recursive enumeration.

            # Simpler: enumerate how many of the a pairs have first-half winner (0..a) = x
            # and how many of the other pairs between have certain outcomes
            # new_f = x + 1 + (1 if n odd and middle < f else 0) ... still complex

            # Let me just use brute force for small n (n <= 28)
            pairs = []
            matched = set()
            mid_player = -1
            for i in range(1, half + 1):
                j = n + 1 - i
                if i == f and j == s or i == s and j == f:
                    # They meet - shouldn't happen (checked above)
                    pass
                elif i == f or j == f:
                    pairs.append(('f', i, j))
                    matched.add(i)
                    matched.add(j)
                elif i == s or j == s:
                    pairs.append(('s', i, j))
                    matched.add(i)
                    matched.add(j)
                else:
                    pairs.append(('o', i, j))
                    matched.add(i)
                    matched.add(j)
            if n % 2 == 1:
                mid_player = half + 1

            # Enumerate all possible outcomes for 'o' pairs
            other_pairs = [p for p in pairs if p[0] == 'o']
            num_other = len(other_pairs)

            for mask in range(1 << num_other):
                winners = set()
                winners.add(f)
                winners.add(s)
                if mid_player > 0:
                    winners.add(mid_player)
                for bit in range(num_other):
                    i, j = other_pairs[bit][1], other_pairs[bit][2]
                    if mask & (1 << bit):
                        winners.add(i)
                    else:
                        winners.add(j)
                sorted_w = sorted(winners)
                new_f = sorted_w.index(f) + 1
                new_s = sorted_w.index(s) + 1
                e, l = dp(nxt, new_f, new_s)
                mn = min(mn, e)
                mx = max(mx, l)

            memo[(n, f, s)] = (mn + 1, mx + 1)
            return (mn + 1, mx + 1)

        return list(dp(n, firstPlayer, secondPlayer))
