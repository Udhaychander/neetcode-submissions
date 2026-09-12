class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res=[]
        for a in asteroids:
            if res and a<0 and res[-1]>0:
                diff=a+res[-1]
                if diff>0:
                    a=0
                elif diff<0:
                    res.pop()
                else:
                    a=0
                    res.pop()
            if a!=0:
                res.append(a)
        return res