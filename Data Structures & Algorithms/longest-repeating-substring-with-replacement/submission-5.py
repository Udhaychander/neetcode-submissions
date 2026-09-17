class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=maxf=res=0
        count=Counter()
        for r,c in enumerate(s):
            count[c]+=1
            maxf=max(maxf,count[c])
            if (r-l+1)-maxf<=k:
                res=r-l+1
        return res

                