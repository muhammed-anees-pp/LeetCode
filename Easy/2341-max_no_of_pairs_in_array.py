# Problem: Maximum Number of Pairs in Array
# Link: https://leetcode.com/problems/maximum-number-of-pairs-in-array/
# Approach: Count the frequency of each number. Each pair is formed by two identical numbers,
# so pairs are calculated using integer division, and leftovers using modulo.

from typing import List

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        freq = {}
        pairs = 0
        leftovers = 0

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        for count in freq.values():
            pairs += count // 2
            leftovers += count % 2

        return [pairs, leftovers]
