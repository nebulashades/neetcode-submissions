class Solution:
    def countSubstrings(self, s: str) -> int:
        if len(s)==0 or s==None:
            return 0

        elif len(s)==1:
            return 1

        


        def checkPalindrome(left, right):
            count = 0
            while left>=0 and right<len(s) and s[left] == s[right]:
                left-=1
                right+=1
                count+=1

            return count

        count = 1
        for i in range(1, len(s)):
            l1 = checkPalindrome(i, i)
            l2 = checkPalindrome(i-1, i)
            print(l1, l2, i)
            count+=l1+l2


        return count
                
        