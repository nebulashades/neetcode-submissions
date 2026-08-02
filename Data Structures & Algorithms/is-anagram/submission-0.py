class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Approach 1 : By sorting
        # Time Complexity: O(n log(n))
        # Space Complexity: O(n)

        if len(s) != len(t):
            return False

        s1 = sorted(s)
        t1 = sorted(t)
        
        for i, j in zip(s1, t1):
            if i != j:
                return False
        return True
