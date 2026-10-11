class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {'(': ')', '[':']', '{':'}'}

        for char in s:
            if char in brackets:
                stack.append(char)
            else:
                if not stack or char!= brackets[stack[-1]]:
                    return False
                stack.pop()

        if len(stack)>0:
            return False
        return True