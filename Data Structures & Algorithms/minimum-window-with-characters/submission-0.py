class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        countT = Counter(t)
        res, resLen = [-1, -1], float("infinity")
        for i in range(len(s)):
            countS = Counter()
            for j in range(i, len(s)):
                countS[s[j]] += 1 
                if all(countS[c] >= countT[c] for c in countT):
                    if (j - i + 1) < resLen:
                        resLen = j - i + 1
                        res = [i, j]
        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""