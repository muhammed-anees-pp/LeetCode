# Problem: Check if Number Has Equal Digit Count and Digit Value
# Link: https://leetcode.com/problems/check-if-number-has-equal-digit-count-and-digit-value/
# Approach: For each index i, check if the digit at index i equals
#           the count of digit i in the string.

class Solution:
    def digitCount(self, num: str) -> bool:
        for i in range(len(num)):
            if int(num[i]) != num.count(str(i)):
                return False
        return True
