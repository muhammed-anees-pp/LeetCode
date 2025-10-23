# Problem: Check If Digits Are Equal in String After Operations I
# Link: https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-i/
# Approach: Repeatedly replace each adjacent pair with their sum modulo 10 until two digits remain, then compare them.

class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while len(s) > 2:
            temp = []
            for i in range(len(s) - 1):
                digit1 = ord(s[i]) - ord('0')
                digit2 = ord(s[i + 1]) - ord('0')
                temp.append(str((digit1 + digit2) % 10))
            s = ''.join(temp)
        return s[0] == s[1]
