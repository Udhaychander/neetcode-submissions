class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = []
        for a in asteroids:
            while res and res[-1] > 0 and a < 0:
                if res[-1] < -a:
                    res.pop()
                    continue
                elif res[-1] == -a:
                    res.pop()
                break
            else:
                res.append(a)
        return res