class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left <= right:
            mid = (left + right) // 2
            hrs = 0
            for i in piles:
                hrs += (i + mid - 1) // mid
            if hrs > h:
                left = mid + 1
            else:
                k = mid
                right = mid - 1

        return k
