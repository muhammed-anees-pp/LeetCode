# Problem: Furthest Point From Origin
# Link: https://leetcode.com/problems/furthest-point-from-origin/
# Approach: Count moves to the left (L), right (R), and blanks (_). 
#           Blanks can be used in the direction that increases the distance.

class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        left = moves.count('L')
        right = moves.count('R')
        blank = moves.count('_')
        return abs(left - right) + blank
