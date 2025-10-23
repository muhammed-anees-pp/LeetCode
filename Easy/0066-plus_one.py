# Problem: Plus One
# Link: https://leetcode.com/problems/plus-one/
# Approach: Start from the last digit and add 1. 
# If a digit becomes 10, set it to 0 and carry over to the next digit. 
# If all digits are 9, prepend 1 at the beginning.

from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits
