"""
Problem: 973. K Closest Points to Origin
Date Completed: 7/17/2025
"""

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = []
        # Append the negative distance of each point with the point to the dist array
        for i in points:
            dist.append([-(i[0]**2 + i[1]**2), i[0], i[1]])
        # Turn dist into a min-Heap
        heapq.heapify(dist)
        # While dist is larger than k remove the farthest points from dist
        while len(dist) > k:
            heapq.heappop(dist)
        # Build and return ans array
        ans = []
        for _, x, y in dist:
            ans.append([x, y])
        return ans
