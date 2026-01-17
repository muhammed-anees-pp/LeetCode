# Problem: Minimum Cost of Buying Candies With Discount
# Link: https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount/
# Approach: Sort the costs in descending order. For every group of three candies,
#           add the cost of the first two (the third one is free).

from typing import List

class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        minCost = 0

        for i in range(0, len(cost), 3):
            minCost += cost[i]
            if i + 1 < len(cost):
                minCost += cost[i + 1]

        return minCost
