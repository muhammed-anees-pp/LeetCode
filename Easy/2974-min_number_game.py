# Problem: Minimum Number Game
# Link: https://leetcode.com/problems/minimum-number-game/
# Approach: Sort the array, then repeatedly take the two smallest numbers.
#           Alice picks the smallest, Bob picks the next smallest.
#           Append Bob first, then Alice to the result array.

from typing import List

class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        result = []

        while nums:
            alice = nums.pop(0)
            bob = nums.pop(0)

            result.append(bob)
            result.append(alice)

        return result
