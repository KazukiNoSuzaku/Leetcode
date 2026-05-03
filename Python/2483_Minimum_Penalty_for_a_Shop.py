class Solution:
    def bestClosingTime(self, customers: str) -> int:
        # Penalty at closing hour k: #'N' in [0,k) + #'Y' in [k,n)
        # Scan left to right, maintaining running 'N' count and remaining 'Y' count.
        y_remaining = customers.count('Y')
        best_penalty = y_remaining  # close at hour 0
        best_hour = 0
        n_count = 0

        for i, c in enumerate(customers):
            if c == 'N':
                n_count += 1
            else:
                y_remaining -= 1
            penalty = n_count + y_remaining  # close at hour i+1
            if penalty < best_penalty:
                best_penalty = penalty
                best_hour = i + 1

        return best_hour
