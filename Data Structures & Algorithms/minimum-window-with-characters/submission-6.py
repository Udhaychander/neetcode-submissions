class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count1 = Counter(t)
        count2 = Counter()
        l = 0
        have = 0
        need = len(count1)
        res = ""
        resLen = float("inf")
        for r, c in enumerate(s):
            count2[c] += 1
            if c in count1 and count2[c] == count1[c]:
                have += 1
            while have == need:
                if r - l + 1 < resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                count2[s[l]] -= 1
                if s[l] in count1 and count2[s[l]] < count1[s[l]]:
                    have -= 1
                l += 1
        return res