# Problem: Missing Number
# Link: https://leetcode.com/problems/missing-number/
# Approach: Calculate the expected sum using the formula n*(n+1)//2,
# then subtract the actual sum of the array to find the missing number.

from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total = n * (n + 1) // 2
        current_total = sum(nums)
        return total - current_total
