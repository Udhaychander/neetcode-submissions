class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        store = []
        for n in nums:
            heapq.heappush(store, n)
            if len(store) > k:
                heapq.heappop(store)
        return store[0]