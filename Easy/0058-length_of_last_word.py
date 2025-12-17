# Problem: Length of Last Word
# Link: https://leetcode.com/problems/length-of-last-word/
# Approach: Split the string by spaces and return the length of the last word.

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        return len(words[-1])
