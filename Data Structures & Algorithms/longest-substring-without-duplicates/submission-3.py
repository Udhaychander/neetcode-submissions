class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        store=defaultdict(int)
        res=0
        for r,c in enumerate(s):
            if c in store:
                l=max(store[c]+1,l)
            store[c]=r
            res=max(res,r-l+1)
        return res