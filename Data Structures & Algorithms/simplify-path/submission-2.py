class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        res = []
        for cur in path:
            if cur == "" or cur == ".":
                continue
            elif cur == "..":
                if res:
                    res.pop()
            else:
                res.append(cur)
        return "/" + "/".join(res)