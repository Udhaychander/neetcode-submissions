class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda t: t[1])
        minHeap = []
        curPass = 0
        for numPass, start, end in trips:
            while minHeap and start>=minHeap[0][0] :
                curPass -= heapq.heappop(minHeap)[1]
            curPass += numPass
            if curPass > capacity:
                return False
            heapq.heappush(minHeap, [end, numPass])
        return True