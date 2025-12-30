# Problem: Alternating Digit Sum
# Link: https://leetcode.com/problems/alternating-digit-sum/
# Approach: Convert the number to digits and alternately add and subtract them based on index.

class Solution:
    def alternateDigitSum(self, n: int) -> int:
        digits = [int(d) for d in str(n)]
        total = 0

        for i, digit in enumerate(digits):
            if i % 2 == 0:
                total += digit
            else:
                total -= digit
        
        return total