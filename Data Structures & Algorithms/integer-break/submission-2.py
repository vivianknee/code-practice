class Solution:
    def integerBreak(self, n: int) -> int:
        # for n, get every possible way to sum it
        # keep track of all those numbers product to get a max product each time
        memo = {1:1}
        def dfs(x):
            if x in memo:
                return memo[x]

            res = 0 if x == n else x
            for i in range(1, x):
                val = dfs(i) * dfs(x - i)
                res = max(res, val)
            memo[x] = res
            return memo[x]
        return dfs(n)