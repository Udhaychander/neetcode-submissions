class MinStack:
    def __init__(self):
        self.res=[]
        self.ans=[]

    def push(self, val: int) -> None:
        self.res.append(val)
        if self.ans:
            val=min(val,self.ans[-1])
        self.ans.append(val)

    def pop(self) -> None:
        self.res.pop()
        self.ans.pop()

    def top(self) -> int:
        return self.res[-1]

    def getMin(self) -> int:
        return self.ans[-1]