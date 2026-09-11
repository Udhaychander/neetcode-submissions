class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count=Counter(t)
        window=Counter()
        have=0
        need=len(count)
        l=0
        res=''
        reslen=float('inf')
        for r,c in enumerate(s):
            window[c]+=1
            if c in t and window[c]==count[c]:
                have+=1
            while have==need:
                if r-l+1<reslen:
                    res=s[l:r+1]
                    reslen=r-l+1
                window[s[l]]-=1
                if s[l] in t and window[s[l]]<count[s[l]]:
                    have-=1
                l+=1
        return res