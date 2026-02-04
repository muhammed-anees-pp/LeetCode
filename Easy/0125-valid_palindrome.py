# Problem: Valid Palindrome
# Link: https://leetcode.com/problems/valid-palindrome/
# Approach: Use two pointers to compare characters from both ends, skipping non-alphanumeric characters.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            elif s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1

        return True
