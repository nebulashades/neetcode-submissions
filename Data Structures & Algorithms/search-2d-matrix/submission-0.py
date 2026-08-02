class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        left = 0
        r = len(matrix)
        c = len(matrix[0])
        right = r * c - 1

        while left <= right:
            mid = (left + right) // 2
            n = matrix[mid//c][mid % c]
            if target == n:
                return True
            elif target < n:
                right = mid - 1
            else:
                left = mid + 1

        return False
