class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        for char in s:
            if char in "{[(":
                stack.append(char)
            else:
                if not stack: return False
                c = stack.pop()
                if not self.checkBracket(c, char):
                    return False
        if len(stack) > 0: return False
        return True

    def checkBracket(self, char1: str, char2: str) -> bool:
        if char1 == "{" and char2 == "}": return True
        if char1 == "[" and char2 == "]": return True
        if char1 == "(" and char2 == ")": return True
        return False