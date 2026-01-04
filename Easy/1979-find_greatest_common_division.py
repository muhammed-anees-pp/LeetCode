# Problem: Find Greatest Common Divisor of Array
# Link: https://leetcode.com/problems/find-greatest-common-divisor-of-array/
# Approach: Use Python's built-in math.gcd function on the
# minimum and maximum elements of the array.

from typing import List
import math

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        smallest = min(nums)
        largest = max(nums)
        
        return math.gcd(smallest, largest)


# Approach: Find the minimum and maximum values in the array,
# then apply the Euclidean algorithm to compute their GCD.


class Solutions:
    def findGCD(self, nums: List[int]) -> int:
        smallest = min(nums)
        largest = max(nums)
        
        while smallest != 0:
            largest, smallest = smallest, largest % smallest
        
        return largest
