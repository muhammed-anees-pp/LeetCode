# Problem: Two Sum
# Link: https://leetcode.com/problems/two-sum/
# Approach: Use a dictionary (hash map) to store numbers while iterating.

class Solution:
    def twoSum(self, nums, target):
        seen = {}
        for i, num in enumerate(nums):
            if target - num in seen:
                return [seen[target - num], i]
            seen[num] = i
