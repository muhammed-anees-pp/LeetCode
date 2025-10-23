# Problem: Maximum Difference Between Increasing Elements
# Link: https://leetcode.com/problems/maximum-difference-between-increasing-elements/
# Approach: Track the smallest element so far and calculate the maximum difference when a larger number appears.

from typing import List

class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        min_value = nums[0]
        max_difference = -1
        for num in nums[1:]:
            if num > min_value:
                max_difference = max(max_difference, num - min_value)
            min_value = min(min_value, num)
        return max_difference
