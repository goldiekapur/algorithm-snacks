#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# 超时
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        return self.helper(amount, 0, 0, coins)

    def helper(self, amount, idx, temp, coins):
        if temp == amount:
            return 1
        res = 0
        for i in range(idx, len(coins)):
            if temp + coins[i] > amount:
                break
            res += self.helper(amount, i, temp + coins[i], coins)
        return res


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        l = len(coins)
        dp = [[0] * (amount + 1) for _ in range(l + 1)]
        dp[0][0] = 1
        for i in range(1, l + 1):
            dp[i][0] = 1
            for j in range(1, amount + 1):
                dp[i][j] = dp[i - 1][j] + (dp[i][j - coins[i - 1]] if j - coins[i - 1] >= 0 else 0)
        return dp[l][amount]


# O(amount * n)
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        res = 0
        dp = [0] * (amount + 1)
        dp[0] = 1
        for c in coins:
            for i in range(1, amount + 1):
                if i - c >= 0:
                    dp[i] += dp[i - c]
        return dp[-1]
