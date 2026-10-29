class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        m = len(matrix)
        n = len(matrix[0])
        result = []
        for i in range(m):
            for j in range(n):
                result.append(matrix[i][j])
        result.sort()
        return result[k-1]
#Time - O(MN log(MN))
#Space - O(MN)


import heapq
class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        minheap = []
        for row in range(len(matrix)): #N log N
            heapq.heappush(minheap, (matrix[row][0], row, 0)) #logN
        for i in range(k): # k log k
            value, row, col = heapq.heappop(minheap) 
            if col+1 < len(matrix[0]):
                heapq.heappush(minheap, (matrix[row][col+1], row, col+1)) #logN
        return value
# Time - O(N+K(lognN))
# Space - O(M) where M is the number of rows

class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        m = len(matrix)
        n = len(matrix[0])
        left = matrix[0][0]
        right = matrix[-1][-1]
        while left < right:
            mid = (left + right) // 2
            count = 0
            row = 0
            col = n-1
            while row < m and col >= 0:
                if matrix[row][col] <= mid:
                    count += col + 1
                    row += 1
                else:
                    col -= 1
            if count < k:
                left = mid + 1
            else:
                right = mid
        return left