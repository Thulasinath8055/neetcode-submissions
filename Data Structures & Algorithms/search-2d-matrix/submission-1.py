class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1

        # Find row
        while l <= r:
            mid = (l + r) // 2

            if matrix[mid][0] <= target:
                l = mid + 1
            else:
                r = mid - 1

        row = r

        # Search in row
        left = 0
        right = len(matrix[row]) - 1
        flag = False

        while left <= right:
            mid = (left + right) // 2

            if matrix[row][mid] < target:
                left = mid + 1
            elif matrix[row][mid] > target:
                right = mid - 1
            else:
                flag = True
                break

        return flag
        