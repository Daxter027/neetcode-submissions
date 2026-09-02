class Solution:
    def isValid(self, s: str) -> bool:
        lstart = ['(','[','{']
        lend = [')',']','}']
        brackets = {')': '(', ']': '[', '}': '{'}
        stack = []
        for i in s:
            if i in lstart:
                stack.append(i)
            elif len(stack) == 0 and i in lend:
                return False
            else:
                if stack[-1] == brackets.get(i):
                    stack.pop()
                else:
                    return False
        return len(stack)==0;
        