# Problem: Check if All Characters Have Equal Number of Occurrences
# Link: https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/
# Approach: Count character frequencies using Counter and check if all counts are the same.

from collections import Counter

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        freq = Counter(s)
        return len(set(freq.values())) == 1
