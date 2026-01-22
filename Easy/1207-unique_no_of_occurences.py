# Problem: Unique Number of Occurrences
# Link: https://leetcode.com/problems/unique-number-of-occurrences/
# Approach: Count occurrences using a dictionary and check if all counts are unique using a set.

from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count_map = {}

        for num in arr:
            count_map[num] = count_map.get(num, 0) + 1

        seen = set()
        for count in count_map.values():
            if count in seen:
                return False
            seen.add(count)

        return True
