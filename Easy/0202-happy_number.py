# Problem: Happy Number
# Link: https://leetcode.com/problems/happy-number/
# Approach: Use Floyd’s Cycle Detection (slow & fast pointers) to detect cycles
#           while repeatedly replacing the number with the sum of squares of its digits.

class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(num: int) -> int:
            total = 0
            while num > 0:
                digit = num % 10
                total += digit * digit
                num //= 10
            return total

        slow = fast = n
        while fast != 1:
            slow = get_next(slow)
            fast = get_next(get_next(fast))
            if slow == fast:
                return False

        return True
