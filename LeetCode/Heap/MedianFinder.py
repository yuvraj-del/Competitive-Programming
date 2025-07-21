"""
Problem: 295. Find Median from Data Stream
Date Completed: 7/21/2025
"""

class MedianFinder:

    # Initialize min and max heaps and heapify them
    def __init__(self):
        self.minHeap = []
        heapq.heapify(self.minHeap)
        self.maxHeap = []
        heapq.heapify(self.maxHeap)

    def addNum(self, num: int) -> None:
        # Add num to maxHeap if it has no elements or num is smaller than the max
        if not self.maxHeap or num <= -self.maxHeap[0]:
            heapq.heappush(self.maxHeap, -num)
        # Else add num to minHeap
        else:
            heapq.heappush(self.minHeap, num)
        # If the length of the 2 heaps is off by 2 then they need to be rebalanced
        if abs(len(self.minHeap) - len(self.maxHeap)) == 2:
            # If minHeap is bigger than add the min to max
            if len(self.minHeap) > len(self.maxHeap):
                heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))
            # Else add the max value of maxHeap to minHeap
            else:
                heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
        
    def findMedian(self) -> float:
        # If one of the heap is bigger they hold the median at their root
        if len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        elif len(self.minHeap) < len(self.maxHeap):
            return -self.maxHeap[0]
        # Else calculate the median with the 2 heaps
        else:
            return (-self.maxHeap[0] + self.minHeap[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
