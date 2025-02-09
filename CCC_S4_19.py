def max_total_score(n, k, scores):
    from functools import lru_cache  # To memoize results

    # Recursive function to find the max total score from index i to end
    @lru_cache(None)  # Cache results for efficiency
    def dp(i):
        if i >= n:  # Base case: no attractions left
            return 0

        max_score = 0
        best_total = 0

        # Try all possible group sizes (1 to k)
        for j in range(1, min(k, n - i) + 1):
            max_score = max(max_score, scores[i + j - 1])  # Max in current group
            best_total = max(best_total, max_score + dp(i + j))  # Choose best split

        return best_total

    return dp(0)  # Start from index 0

# Input reading
line1 = input().split()
n = int(line1[0])  # Number of attractions
k = int(line1[1])  # Maximum attractions per day

scores = list(map(int, input().split()))  # Convert input to list of integers

print(max_total_score(n, k, scores))  # Output the max total score