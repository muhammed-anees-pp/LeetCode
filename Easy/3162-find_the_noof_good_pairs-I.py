# Problem: Find the Number of Good Pairs I
# Link: https://leetcode.com/problems/find-the-number-of-good-pairs-i/
# Approach: Use two nested loops to check all possible pairs.
#           If nums1[i] is divisible by nums2[j] * k, count it as a good pair.

from typing import List

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        goodCount = 0
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] % (nums2[j] * k) == 0:
                    goodCount += 1
        return goodCount
