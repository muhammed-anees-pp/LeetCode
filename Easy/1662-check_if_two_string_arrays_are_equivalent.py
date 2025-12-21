# Problem: Check If Two String Arrays are Equivalent
# Link: https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/
# Approach: Join all strings in each array to form two complete strings and compare them.

from typing import List

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        string1 = ""
        string2 = ""

        for char in word1:
            string1 += char
        
        for char in word2:
            string2 += char
        
        return string1 == string2
