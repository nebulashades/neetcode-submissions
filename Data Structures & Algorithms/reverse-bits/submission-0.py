class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0

        i= 0 
        while i<32:
            if ((n>>i) &1)==1:
                ans = ans | (1 << (31 - i))
            i+=1

        return ans

        