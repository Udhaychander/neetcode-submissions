class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = []
        for a in asteroids:
            alive = True
            while res and a < 0 and res[-1] > 0:
                if res[-1] > -a:
                    alive = False
                    break
                elif res[-1] < -a:
                    res.pop()
                else:
                    res.pop()
                    alive = False
                    break
            if alive:
                res.append(a)
        return res