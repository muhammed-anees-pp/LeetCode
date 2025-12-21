# Problem: Sum of Squares of Special Elements
# Link: https://leetcode.com/problems/sum-of-squares-of-special-elements/
# Approach: Iterate through the array and check if the index (1-based) divides the array length.
#           If it does, add the square of that element to the total.

from typing import List

class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0
        for i in range(n):
            if n % (i + 1) == 0:
                total += nums[i] * nums[i]
        return total
