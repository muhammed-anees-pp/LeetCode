# Problem: Create Target Array in the Given Order
# Link: https://leetcode.com/problems/create-target-array-in-the-given-order/
# Approach: Iterate through nums and insert each element at its given index.

from typing import List

class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            result.insert(index[i], nums[i])
        return result
