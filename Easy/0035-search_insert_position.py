# Problem: Search Insert Position
# Link: https://leetcode.com/problems/search-insert-position/
# Approach: Use binary search to find the target index. If not found, return the position where it should be inserted.

from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return left
