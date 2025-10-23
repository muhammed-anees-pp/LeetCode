# Problem: Longest Common Prefix
# Link: https://leetcode.com/problems/longest-common-prefix/
# Approach: Start with the first string as prefix and compare it with each string.
# If a string doesn't start with the current prefix, shorten the prefix until it matches.

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        prefix = strs[0]
        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix
