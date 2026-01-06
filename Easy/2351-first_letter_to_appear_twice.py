# Problem: First Letter to Appear Twice
# Link: https://leetcode.com/problems/first-letter-to-appear-twice/
# Approach: Use a set to track seen characters. 
#           Return the first character that appears again.

from typing import Set

class Solution:
    def repeatedCharacter(self, s: str) -> str:
        seen: Set[str] = set()
        
        for char in s:
            if char in seen:
                return char
            seen.add(char)
