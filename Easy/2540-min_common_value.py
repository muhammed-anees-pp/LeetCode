# Problem: Minimum Common Value
# Link: https://leetcode.com/problems/minimum-common-value/
# Approach: Use two pointers to traverse both sorted arrays and find the smallest common element.

from typing import List

class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i = j = 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                return nums1[i]
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        
        return -1