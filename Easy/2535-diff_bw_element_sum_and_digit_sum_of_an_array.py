# Problem: Difference Between Element Sum and Digit Sum of an Array
# Link: https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array/
# Approach: 
#   - Calculate the sum of all elements in the array.
#   - Calculate the sum of all digits of each element.
#   - Return the difference between the two sums.

from typing import List

class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        element_sum = sum(nums)
        digit_sum = sum(int(digit) for num in nums for digit in str(num))
        return element_sum - digit_sum
