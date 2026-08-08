class Solution:
    def minWindow(self, s: str, t: str) -> str:

        target = {}
        for i in t:
            target[i] = target.get(i, 0) + 1

        count = {}
        left = 0

        min_len = float("inf")
        start = -1
        current = 0

        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            if s[right] in target and count[s[right]] == target[s[right]]:
                current += 1

            while current == len(target):
                size = right - left + 1
                if size < min_len:
                    min_len = size
                    start = left

                count[s[left]] -= 1
                if s[left] in target and count[s[left]] < target[s[left]]:
                    current -= 1
                left += 1

        if start == -1:
            return ""

        return s[start : start + min_len]
