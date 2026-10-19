class Solution:
    def minRooms(self, intervals: List[List[int]]):
        if not intervals:
            return 0
        intervals.sort()
        minheap = [intervals[0][1]]
        for i in range(1, len(intervals)):
            if intervals[i][0] >= minheap[0]:
                heapq.heappop(minheap)
            heapq.heappush(minheap, intervals[i][1])
        return len(minheap)
#Time - O(NlogN)
#Space - O(N)

class Solution:
    def minRooms(self, intervals: List[List[int]]):
        count = 0
        if not intervals:
            return count
        starttime = sorted(interval[0] for interval in intervals)
        endtime = sorted(interval[1] for interval in intervals)
        p1 = 0
        p2 = 0
        while p1 < len(starttime):
            if starttime[p1] < endtime[p2]:
                count += 1
            else:
                p2 += 1
            p1 += 1
        return count
#Time - O(NlogN)
#Space - O(N)