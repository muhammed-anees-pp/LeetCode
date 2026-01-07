# Problem: Two Sum II - Input Array Is Sorted
# Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# Approach: Use a hash map to store seen numbers and find the complement.

from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(numbers):
            if target - num in seen:
                return [seen[target - num] + 1, i + 1]
            seen[num] = i
