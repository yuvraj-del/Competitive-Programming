"""
Problem: 621. Task Scheduler
Date Completed: 7/17/2025
"""

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Frequency of each letter in tasks
        freq = defaultdict(int)
        for i in tasks:
            freq[i] += 1
        # Create a min-heap of the negative of each letter's frequency
        nums = []
        for k, v in freq.items():
            nums.append(-v)
        heapq.heapify(nums)
        queue = []
        time = 0
        # While tasks or cooling tasks are still remaining 
        while nums or queue:
            # Increment time
            time += 1
            # If a task is remaining
            if nums:
                count = heapq.heappop(nums) + 1
                # Add to queue if frequency of task is not 0
                if count != 0:
                    queue.append([count, time + n])
            # If a task is done cooling
            if queue and queue[0][1] == time:
                # Remove the task
                temp = queue.pop(0)
                # If task is still remaining add it back to nums
                if temp[0] < 0:
                    heapq.heappush(nums, temp[0])
        return time
