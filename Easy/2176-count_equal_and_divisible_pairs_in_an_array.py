# Problem: Count Equal and Divisible Pairs in an Array
# Link: https://leetcode.com/problems/count-equal-and-divisible-pairs-in-an-array/
# Approach: Use two nested loops to check every valid pair (i, j).
#           If nums[i] == nums[j] and (i * j) is divisible by k, increment the count.

from typing import List

class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        n = len(nums)
        result = 0

        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] == nums[j] and (i * j) % k == 0:
                    result += 1

        return result