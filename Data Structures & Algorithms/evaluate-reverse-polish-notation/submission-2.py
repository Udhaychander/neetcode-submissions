class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c in {"+", "-", "*", "/"}:
                b = stack.pop()  # right operand
                a = stack.pop()  # left operand

                if c == "+":
                    stack.append(a + b)
                elif c == "-":
                    stack.append(a - b)
                elif c == "*":
                    stack.append(a * b)
                else:  # division
                    stack.append(int(a / b))  # truncates toward zero
            else:
                stack.append(int(c))

        return stack[0]
