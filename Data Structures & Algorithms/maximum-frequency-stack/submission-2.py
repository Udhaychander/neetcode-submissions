class FreqStack:

    def __init__(self):
        self.res=[]
        self.count=Counter()

    def push(self, val: int) -> None:
        self.res.append(val)
        self.count[val]+=1

    def pop(self) -> int:
        maxf = max(self.count.values())
        i = len(self.res) - 1
        while i>=0:
            if self.count[self.res[i]] == maxf:
                self.count[self.res[i]] -= 1
                return self.res.pop(i)
            i -= 1