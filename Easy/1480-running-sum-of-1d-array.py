# Problem: Running Sum of 1d Array
# Link: https://leetcode.com/problems/running-sum-of-1d-array/
# Approach: Iterate through the array, keep a running sum, and append it to a new list.

from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        total = 0
        for num in nums:
            total += num
            result.append(total)
        return result
