class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair=([p,s] for p,s in zip(position,speed))
        res=[]
        for p,s in sorted(pair):
            res.append((target-p)/s)
            while len(res)>=2 and res[-1]>=res[-2]:
                res.pop(-2)
        return len(res)