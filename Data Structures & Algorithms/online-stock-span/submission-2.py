class StockSpanner:

    def __init__(self):
        self.res=[]
    def next(self, price: int) -> int:
        span=1
        while self.res and price>=self.res[-1][0]:
            span+=self.res[-1][1]
            self.res.pop()
        self.res.append([price,span])
        return span