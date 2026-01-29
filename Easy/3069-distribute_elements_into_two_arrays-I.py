# Problem: Distribute Elements Into Two Arrays I
# Link: https://leetcode.com/problems/distribute-elements-into-two-arrays-i/
# Approach: Start by placing the first two elements into two separate arrays.
# For the remaining elements, compare the last elements of both arrays and
# append the current element to the array with the larger last value.

from typing import List

class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1 = []
        arr2 = []

        for i in range(len(nums)):
            if i == 0:
                arr1.append(nums[i])
            elif i == 1:
                arr2.append(nums[i])
            else:
                if arr1[-1] > arr2[-1]:
                    arr1.append(nums[i])
                else:
                    arr2.append(nums[i])

        return arr1 + arr2
