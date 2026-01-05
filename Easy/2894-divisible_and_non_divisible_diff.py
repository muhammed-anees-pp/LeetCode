# Problem: Divisible and Non-divisible Sums Difference
# Link: https://leetcode.com/problems/divisible-and-non-divisible-sums-difference/
# Approach: Iterate from 1 to n, add divisible numbers to one sum and non-divisible numbers to another.

class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        divisible_sum = 0
        non_divisible_sum = 0

        for i in range(1, n + 1):
            if i % m == 0:
                divisible_sum += i
            else:
                non_divisible_sum += i

        return non_divisible_sum - divisible_sum
