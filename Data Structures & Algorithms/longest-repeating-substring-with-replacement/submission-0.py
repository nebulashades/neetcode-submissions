class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        max_len = 0

        unique = {}
        left = 0
        max_freq = 0

        for right in range(len(s)):
            unique[s[right]] = unique.get(s[right], 0) + 1
            if unique[s[right]] > max_freq:
                max_freq = max(max_freq, unique[s[right]])
            size = right - left + 1

            while size - max_freq > k:
                unique[s[left]] -= 1
                if unique[s[left]] < 0:
                    del unique[s[left]]
                max_freq = max(unique.values())
                size -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len
