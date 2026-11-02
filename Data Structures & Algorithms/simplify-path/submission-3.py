class Solution:
    def simplifyPath(self, path: str) -> str:
        res = []
        paths = path.split('/')
        for p in paths:
            if p == '..':
                if res:
                    res.pop()
            elif p != '.' and p != '':
                res.append(p)
        return '/' + '/'.join(res)