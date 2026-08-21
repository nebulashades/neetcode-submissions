class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ans = 0

        def operation(a, b, i):
            if i == "+":
                return a + b
            elif i == "-":
                return a - b
            elif i == "*":
                return a * b
            elif i == "/":
                return int(a / b)

        for i in tokens:
            if i in "+-*/":
                a = stack.pop()
                b = stack.pop()
                ans = operation(b, a, i)
                stack.append(ans)
            else:
                stack.append(int(i))

        return stack.pop()
