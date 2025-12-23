# Problem: Sort Array By Parity
# Link: https://leetcode.com/problems/sort-array-by-parity/
# Approach: Traverse the array, separate even and odd numbers into two lists,
#           and then concatenate even numbers first followed by odd numbers.

from typing import List

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even = [x for x in nums if x % 2 == 0]
        odd = [x for x in nums if x % 2 != 0]
        return even + odd
