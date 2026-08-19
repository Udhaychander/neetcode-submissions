class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        store = defaultdict()
        l = 0
        res = 0
        for r in range(len(s)):
            if s[r] in store:
                l = max(store[s[r]] + 1, l)
            store[s[r]] = r
            res = max(res, r - l + 1)
        return res