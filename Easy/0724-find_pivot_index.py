# Problem: Find Pivot Index
# Link: https://leetcode.com/problems/find-pivot-index/
# Approach: Calculate the total sum first. Then, iterate through the array while keeping track of the left and right sums. 
# The pivot index is found when both sides are equal.

from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        right_total = sum(nums)
        left_total = 0

        for i, num in enumerate(nums):
            right_total -= num
            if left_total == right_total:
                return i
            left_total += num
        return -1
