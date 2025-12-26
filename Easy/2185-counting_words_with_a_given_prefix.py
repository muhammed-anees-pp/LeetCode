# Problem: Counting Words With a Given Prefix
# Link: https://leetcode.com/problems/counting-words-with-a-given-prefix/
# Approach: Iterate through each word and count how many start with the given prefix.

from typing import List

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        for word in words:
            if word.startswith(pref):
                count += 1
        return count