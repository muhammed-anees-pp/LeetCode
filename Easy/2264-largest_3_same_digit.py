# Problem: Largest 3-Same-Digit Number in String
# Link: https://leetcode.com/problems/largest-3-same-digit-number-in-string/
# Approach: Scan the string and check every group of 3 consecutive characters.
#           If all three are equal, form a 3-digit string and keep track
#           of the maximum such "good" integer.

class Solution:
    def largestGoodInteger(self, num: str) -> str:
        good = ""
        for i in range(len(num) - 2):
            if num[i] == num[i+1] == num[i+2]:
                good = max(good, num[i] * 3)
        return good
