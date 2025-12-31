# Problem: Largest Positive Integer That Exists With Its Negative
# Link: https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/
# Approach: Use a set for fast lookup and track the largest valid number.

from typing import List

class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        num_set = set(nums)
        largest = -1

        for num in nums:
            if num > 0 and -num in num_set:
                largest = max(largest, num)

        return largest