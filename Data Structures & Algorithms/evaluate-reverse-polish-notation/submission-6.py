class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = 0
        stack = []
        for i in tokens:
            if i not in "+-*/":
                stack.append(i)
            
            if i == "+":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(a)+int(b))
            if i == "*":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(a)*int(b))
            if i == "/":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(int(b)/int(a)))
            if i == "-":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b)-int(a))
        print(stack)
        return int(stack[0])            