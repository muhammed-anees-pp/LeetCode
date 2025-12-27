# Problem: Shuffle String
# Link: https://leetcode.com/problems/shuffle-string/
# Approach: Create a new list of characters and place each character from the
#           original string at its target index, then join the list into a string.

from typing import List

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        shuffled = [''] * len(s)
        
        for i, index in enumerate(indices):
            shuffled[index] = s[i]
        
        return ''.join(shuffled)