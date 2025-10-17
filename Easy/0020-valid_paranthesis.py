# Problem: Valid Parentheses
# Link: https://leetcode.com/problems/valid-parentheses/
# Approach: Use a stack to check matching pairs of parentheses. Push opening brackets onto the stack and pop when a matching closing bracket appears.

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', ']': '[', '}': '{'}
        
        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)
                
        return not stack
