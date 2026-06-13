class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = "".join(c.lower() for c in s if c.isalnum())
        new_s = word[::-1]
        return new_s == word