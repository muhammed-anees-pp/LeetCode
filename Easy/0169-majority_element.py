# Problem: Majority Element
# Link: https://leetcode.com/problems/majority-element/
# Approach: Use the Boyer-Moore Voting Algorithm to find the majority element in linear time.

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0
        
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1
        
        return candidate
