# Problem: Smallest Even Multiple
# Link: https://leetcode.com/problems/smallest-even-multiple/
# Approach: If n is even, return n; otherwise return 2 * n.

class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n % 2 == 0:
            return n
        return n * 2
