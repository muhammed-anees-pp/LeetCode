# Problem: Single Number
# Link: https://leetcode.com/problems/single-number/
# Approach: Use XOR to find the unique element. 
# Since a ^ a = 0 and a ^ 0 = a, all duplicate numbers cancel out, leaving the single number.

from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result
