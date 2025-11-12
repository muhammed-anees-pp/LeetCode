# Problem: Permutations
# Link: https://leetcode.com/problems/permutations/
# Approach: Use backtracking to generate all possible arrangements of numbers by swapping elements.

from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start):
            # Base case: if we’ve fixed all positions, record the permutation
            if start == len(nums):
                result.append(nums[:])
                return
            
            # Try placing each remaining element at the current position
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]  # Swap
                backtrack(start + 1)                         # Recurse
                nums[start], nums[i] = nums[i], nums[start]  # Backtrack (undo swap)

        result = []
        backtrack(0)
        return result
