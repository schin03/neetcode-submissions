class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = "".join(c.lower() for c in s if c.isalnum())
        print(word)
        for i in range(len(word)//2):
            if word[i] != word[len(word)-1-i]:
                return False
        return True