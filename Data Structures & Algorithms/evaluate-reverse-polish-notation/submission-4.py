class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = []
        for c in tokens:
            if c == "+":
                res.append(res.pop() + res.pop())
            elif c == "-":
                b, a = res.pop(), res.pop()
                res.append(a-b)
            elif c == "*":
                res.append(res.pop() * res.pop())
            elif c == "/":
                b,a = res.pop(), res.pop()
                res.append(int(a / b))
            else:
                res.append(int(c))
        return res[0]