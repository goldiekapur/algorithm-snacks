#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()


# https://leetcode.com/problems/confusing-number-ii/

#  超时！
class Solution:
    def confusingNumberII(self, n: int) -> int:

        res = 0
        sub = {0: 0, 1: 1, 9: 6, 8: 8, 6: 9}
        stack = collections.deque([1, 9, 8, 6])
        while stack:
            m = stack.popleft()
            if self.confuse(m, sub) != m:
                res += 1
            m *= 10
            for i in sub:
                if m + i <= n:
                    stack.append(m + i)
        return res

    def confuse(self, a, sub):
        b = 0
        while a > 0:
            b = b * 10 + sub[a % 10]
            a //= 10
        return b



