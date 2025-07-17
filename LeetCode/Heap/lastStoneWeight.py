"""
Problem: 1046. Last Stone Weight
Date Completed: 7/16/2025
"""

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Make all values negative, so min-heap basically becomes max-heap
        stones = [-i for i in stones]
        # Turn stones into a heap
        heapq.heapify(stones)
        # While we still have values in stone
        while len(stones) > 1:
            # Get 1st and 2nd largest stone
            y = heapq.heappop(stones)
            x = heapq.heappop(stones)
            # If stones are different than add difference to heap
            if x != y:
                heapq.heappush(stones, y-x)
        # If stones has a value return it
        if stones:
            return -stones[0]
        # Else return 0
        else:
            return 0
