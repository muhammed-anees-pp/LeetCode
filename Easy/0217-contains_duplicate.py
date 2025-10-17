# Problem: Contains Duplicate
# Link: https://leetcode.com/problems/contains-duplicate/
# Approach: Convert the list to a set and compare lengths.
# If duplicates exist, the set will be smaller since sets remove duplicates.

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) > len(set(nums))
