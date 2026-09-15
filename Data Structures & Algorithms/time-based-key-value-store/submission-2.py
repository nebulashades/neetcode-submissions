class TimeMap:

    def __init__(self):
        self.tmap={}        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.tmap:
           self.tmap[key] =[(timestamp, value)]
        else:
            self.tmap[key].append((timestamp, value))
    
    def get(self, key: str, timestamp: int) -> str:
        if not key in self.tmap:
            return ""
        
        left = 0
        right = len(self.tmap[key])-1
        ans = -1
        
        while left <= right:
            mid = (left +right)//2
            if self.tmap[key][mid][0] <= timestamp:
                ans=mid
                left=mid+1
            else:
                right=mid-1

        if ans != -1:
            return self.tmap[key][ans][1]
        else:
            return ""

        
