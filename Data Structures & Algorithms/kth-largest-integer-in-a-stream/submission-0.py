class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k=k
        self.store=nums

    def add(self, val: int) -> int:
        self.store.append(val)
        self.store.sort()
        return self.store[len(self.store)-self.k]        
