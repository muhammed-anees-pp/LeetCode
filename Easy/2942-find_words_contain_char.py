# Problem: Find Words Containing Character
# Link: https://leetcode.com/problems/find-words-containing-character/
# Approach: Iterate through the list of words and store indices where the given character exists.

from typing import List

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        result = []
        for i in range(len(words)):
            if x in words[i]:
                result.append(i)
        return result
