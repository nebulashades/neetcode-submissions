class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n =len(s)
        inDict = [0 for i in range(n+1)]
        inDict[0]=1

        # abcd
        # 0123
        # a bc d
        #  abcd
        # 11011
        # 01234
        
        for i in range(n):
            j = 0
            while j <= i:
                if inDict[j] and s[j:i+1] in wordDict:
                    inDict[i+1]=1
                    break
                j+=1
        return bool(inDict[n])
            




                    






                





            




           

           


                
        