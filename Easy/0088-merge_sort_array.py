# Problem: Merge Sorted Array
# Link: https://leetcode.com/problems/merge-sorted-array/
# Approach: Use three pointers starting from the end of both arrays.
# Compare elements from nums1 and nums2, and place the larger one
# at the end of nums1 to avoid overwriting existing values.

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i, j, k = m - 1, n - 1, m + n - 1

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
