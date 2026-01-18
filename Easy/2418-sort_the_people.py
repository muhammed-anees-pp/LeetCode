# Problem: Sort the People
# Link: https://leetcode.com/problems/sort-the-people/
# Approach: Map heights to names, sort heights in descending order, and build the result list.

from typing import List

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        heightMap = dict(zip(heights, names))
        sortedHeight = sorted(heights, reverse=True)
        sortedNames = [heightMap[height] for height in sortedHeight]
        return sortedNames
