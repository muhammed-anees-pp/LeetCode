# Problem: Largest Odd Number in String
# Link: https://leetcode.com/problems/largest-odd-number-in-string/
# Approach: Traverse the string from right to left and return the prefix ending at the first odd digit.

class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num) - 1, -1, -1):
            if int(num[i]) % 2 == 1:
                return num[:i + 1]
        return ""
