
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        #   9 1 4 2 3 3 7
        #   9 - 1 - 1 4 - 1 2 - 1 2 3 - 1 2 3 - 1 2 3 7

        def binary_search(s, i):
            left = 0
            right = len(s)-1

            while left <= right:
                mid = (left+right)//2
                if s[mid]==i:
                    return mid
                elif s[mid]>i:
                    right = mid - 1
                else:
                    left = mid + 1

            return left
 
        sequence = [0] * len(nums)
        sequence[0]=nums[0]
        longest = 0
        
        for i in range(1, len(nums)):
            if nums[i]<sequence[longest]:
                j = binary_search(sequence[:longest+1], nums[i])
                sequence[j]=nums[i]
            elif nums[i]>sequence[longest]:
                longest+=1
                sequence[longest]=nums[i]

        return longest+1
                
