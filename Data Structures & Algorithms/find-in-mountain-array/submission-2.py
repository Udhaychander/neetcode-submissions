class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        l,r=1,mountainArr.length()-1
        while l<=r:
            m=(l+r)//2
            if mountainArr.get(m-1)<mountainArr.get(m)>mountainArr.get(m+1):
                break
            elif mountainArr.get(m-1)>mountainArr.get(m)>mountainArr.get(m+1):
                r=m-1
            else:
                l=m+1
        peak=m
        l,r=0,peak-1
        while l<=r:
            m=(l+r)//2
            if mountainArr.get(m)==target:
                return m
            elif mountainArr.get(m)>target:
                r=m-1
            else :
                l=m+1
        l,r=peak,mountainArr.length()-1
        while l<=r:
            m=(l+r)//2
            if mountainArr.get(m)==target:
                return m
            elif mountainArr.get(m)<target:
                r=m-1
            else :
                l=m+1
        return -1