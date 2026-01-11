# Problem: Find Minimum Operations to Make All Elements Divisible by Three
# Link: https://leetcode.com/problems/find-minimum-operations-to-make-all-elements-divisible-by-three/
# Approach: Count how many elements are not divisible by 3.
# Each such element requires exactly one operation to make it divisible by 3.

from typing import List

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            if num % 3 != 0:
                count += 1
        return count
