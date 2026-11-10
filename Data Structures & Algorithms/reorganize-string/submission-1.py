class Solution:
    def reorganizeString(self, s: str) -> str:
        res = list(s)
        i = 1
        while i < len(res):
            if res[i] == res[i - 1]:
                char = res.pop(i)
                for j in range(len(res) + 1):
                    if (j == 0 or res[j - 1] != char) and (j == len(res) or res[j] != char):
                        res.insert(j, char)
                        break
                else:
                    return ""
                i = 1
            else:
                i += 1
        return "".join(res)