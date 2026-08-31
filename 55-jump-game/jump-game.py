from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        farthest = 0  # furthest index we can reach so far

        for i in range(n):
            # If current index is beyond furthest reachable, we're stuck
            if i > farthest:
                return False

            # Update the furthest reachable index
            farthest = max(farthest, i + nums[i])

            # If we can already reach the last index, return True
            if farthest >= n - 1:
                return True

        return True