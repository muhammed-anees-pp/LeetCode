# Problem: Distribute Candies
# Link: https://leetcode.com/problems/distribute-candies/
# Approach: 
# The sister can eat only n/2 candies.
# To maximize the number of different types she eats,
# take the minimum of (n/2) and the number of unique candy types.

from typing import List

class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        n = len(candyType)
        max_candies = n // 2
        unique_types = len(set(candyType))
        return min(max_candies, unique_types)
