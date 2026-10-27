class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count1=Counter(t)
        count2=Counter()
        l=0
        res=''
        have =0
        need=len(count1)
        reslen=float('inf')
        for r,c in enumerate(s):
            count2[c]+=1
            if count1[c]==count2[c]:
                have+=1
            while have==need:
                if reslen>r-l+1:
                    res=s[l:r+1]
                    reslen=r-l+1
                count2[s[l]]-=1
                if count1[s[l]]>count2[s[l]]:
                    have-=1
                l+=1
        return res