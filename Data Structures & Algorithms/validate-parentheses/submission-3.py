class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {'(': ')', '[':']', '{':'}'}

        for char in s:
            if char in brackets.keys():
                stack.append(char)
            else:
                try:
                    if char!= brackets[stack[-1]]:
                        return False
                except IndexError:
                    return False
                stack.pop(-1)

        if len(stack)>0:
            return False
        return True