class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Approach 2 : Using hashmap
        # Time Complexity: O(n+m)
        # Space Complexity: O(k) 
        
        if len(s) != len(t):
            return False

        hashmap ={}
        
        for i in s:
            if i not in hashmap:
                hashmap[i]=0
            hashmap[i]+=1

        for i in t:
            if i not in hashmap:
                return False
            hashmap[i]-=1
            if hashmap[i]<0:
                return False
        return True
