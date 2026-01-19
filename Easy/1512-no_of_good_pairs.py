# Problem: Number of Good Pairs
# Link: https://leetcode.com/problems/number-of-good-pairs/
# Approach: Use two nested loops to compare each pair of elements and count
#           how many pairs (i, j) satisfy nums[i] == nums[j] and i < j.

from typing import List

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    count += 1
        return count
