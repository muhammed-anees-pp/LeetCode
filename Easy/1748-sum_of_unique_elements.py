# Problem: Sum of Unique Elements
# Link: https://leetcode.com/problems/sum-of-unique-elements/
# Approach: Count occurrences of each number and sum only those that appear once.

from typing import List

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        total = 0
        for num in nums:
            if nums.count(num) == 1:
                total += num
        return total
