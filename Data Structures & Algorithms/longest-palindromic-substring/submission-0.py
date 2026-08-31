class Solution:
    def longestPalindrome(self, s: str) -> str:

        if s==None:
            return 0
        elif len(s)==1:
            return s

        def checkPalindrome(left, right):           
            while left>=0 and right < len(s) and s[left]==s[right]:
                left-=1
                right+=1
            return right - left - 1

        start = 0
        max_len = 0
        for i in range(len(s)-1):
            l1 = checkPalindrome(i, i)
            l2 = checkPalindrome(i, i+1) 
            ml = max(l1, l2)
            if ml > max_len:
                max_len = max(l1, l2)
                start = i - ((max_len-1)//2)

        return s[start:start+max_len]



    
        
        