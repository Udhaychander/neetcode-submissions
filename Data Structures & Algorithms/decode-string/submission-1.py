class Solution:
    def decodeString(self, s: str) -> str:
        stack = [] 
        for letter in s:
            if letter == ']':
                seq = deque() 
                while stack and stack[-1] != '[':
                    seq.appendleft(stack.pop())
                stack.pop()
                num = deque() 
                while stack and stack[-1].isnumeric():
                    num.appendleft(stack.pop())
                stack.append(''.join(seq) * int(''.join(num)))
            else:
                stack.append(letter)
        return ''.join(stack)