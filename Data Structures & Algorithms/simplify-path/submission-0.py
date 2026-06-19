class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        paths = path.split('/')

        for cur in paths:
            if cur == "" or cur == ".":
                continue
            elif cur == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(cur)

        return "/" + "/".join(stack)
