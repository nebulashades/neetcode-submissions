class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort()

        ans = intervals[0]
        res = []

        for i in intervals:
            if i[0] <= ans[1]:
                ans[1] = max(i[1], ans[1])
            else:
                res.append(ans)
                ans = i

        res.append(ans)

        return res
