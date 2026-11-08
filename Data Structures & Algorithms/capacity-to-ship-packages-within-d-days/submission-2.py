class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l,r=max(weights),sum(weights)
        res=max(weights)
        while l<=r:
            m=(l+r)//2
            d=1
            load=0
            for w in weights:
                if load+w>m:
                    d+=1
                    load=0
                load+=w
            if d>days:
                l=m+1
            else:
                res=m
                r=m-1
        return res