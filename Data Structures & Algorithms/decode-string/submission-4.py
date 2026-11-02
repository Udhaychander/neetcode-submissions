class Solution:
    def decodeString(self, s: str) -> str:
        res=[]
        for c in s:
            if c != ']':
                res.append(c)
            else:
                substr=''
                while res[-1]!='[':
                    substr=res.pop()+substr
                res.pop()
                num=''
                while res and res[-1].isdigit():
                    num=res.pop()+num
                res.append(int(num)*substr)
        return ''.join(res)
