# Problem: Defanging an IP Address
# Link: https://leetcode.com/problems/defanging-an-ip-address/
# Approach: Iterate through the string and replace '.' with '[.]'.

class Solution:
    def defangIPaddr(self, address: str) -> str:
        result = ""
        for char in address:
            if char == ".":
                result += "[.]"
            else:
                result += char
        return result
