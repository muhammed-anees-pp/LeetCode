# Problem: Truncate Sentence
# Link: https://leetcode.com/problems/truncate-sentence/
# Approach: Split the sentence into words, take the first k words, and join them back into a string.

class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        words = s.split()
        return " ".join(words[:k])
