# https://leetcode.com/problems/jump-game/
# 往前移动，记录可以到达的最远的位置max_step，每次移动的范围要小于max_step
# 如果max_step大于等于最后的index，返回true

# Time complexity: O(n)
# Space complexity: O(1)
class Solution:
    def canJump(self, nums: list) -> bool:
        max_step = 0
        i = 0
        while i < len(nums) and i <= max_step:
            max_step = max(max_step, i + nums[i])
            if max_step >= len(nums) - 1:
                return True
            i += 1
        return False


# 第二种greedy的方法，从后往前
# goal是列表的长度，从后到前，看一下有没有点能满足，在当前位置可以到goal，有的话前移goal到这个点，继续。
# 如果goal最后可以为0，表明可以走到。

class Solution2:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] + i >= goal:
                goal = i
        return goal == 0
