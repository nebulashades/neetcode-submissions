class Solution:
    def numDecodings(self, s: str) -> int:
        
        ways = [0 for i in range(len(s)+1)]

        ways[0]=1

        def validTwo(i):
            if s[i-2]=='1' or (s[i-2]=='2' and s[i-1] in '0123456') :
                return 1
            return 0

        for i in range(1, len(s)+1):
            if s[i-1] != '0':
                ways[i] += ways[i-1]
            if i>=2 and validTwo(i):
                ways[i] += ways[i-2] 

        return ways[len(s)]





        