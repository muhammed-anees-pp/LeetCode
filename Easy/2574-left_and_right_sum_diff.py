# Problem: Left and Right Sum Differences
# Link: https://leetcode.com/problems/left-and-right-sum-differences/
# Approach 1: Brute Force
#   - For each index, calculate left sum and right sum using slicing.
#   - Time Complexity: O(n^2)
#   - Space Complexity: O(n)

from typing import List

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        answer = []
        for i in range(len(nums)):
            total = 0
            leftSum = sum(nums[:i])
            rightSum = sum(nums[i+1:])
            total = abs(leftSum - rightSum)
            answer.append(total)
    
        return answer
        

# Approach 2: Optimized Prefix Sum
#   - Calculate total sum once.
#   - Maintain a running left sum and compute right sum dynamically.
#   - Time Complexity: O(n)
#   - Space Complexity: O(n)



class Solutions:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        totalSum = sum(nums)
        leftSum = 0
        answer = []

        for num in nums:
            rightSum = totalSum - leftSum - num
            answer.append(abs(leftSum - rightSum))
            leftSum += num

        return answer
