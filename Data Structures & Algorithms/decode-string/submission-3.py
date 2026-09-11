class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i, l in enumerate(s):
            if l != "]":
                stack.append(l)
            else:
                substr = ""
                while stack[-1] != "[":
                    substr = stack.pop() + substr
                stack.pop()
                k = ""
                k = stack.pop() + k
                stack.append(int(k) * substr)
        return "".join(stack)