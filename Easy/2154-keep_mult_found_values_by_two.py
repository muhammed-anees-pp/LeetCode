# Problem: Keep Multiplying Found Values by Two
# Link: https://leetcode.com/problems/keep-multiplying-found-values-by-two/
# Approach: Convert the list to a set for fast lookup, then keep doubling
#           the original value while it exists in the set.

from typing import List

class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        nums_set = set(nums)

        while original in nums_set:
            original *= 2
        
        return original