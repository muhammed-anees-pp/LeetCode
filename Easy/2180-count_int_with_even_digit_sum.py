# Problem: Count Integers With Even Digit Sum
# Link: https://leetcode.com/problems/count-integers-with-even-digit-sum/
# Approach: Iterate from 1 to num, calculate the digit sum of each number, 
#           and count how many have an even digit sum.

class Solution:
    def countEven(self, num: int) -> int:
        count = 0
        for n in range(1, num + 1):
            digit_sum = sum(int(d) for d in str(n))
            if digit_sum % 2 == 0:
                count += 1
        return count
