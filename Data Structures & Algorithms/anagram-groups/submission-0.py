class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res =[]
        m = {}

        for s in strs:
            srtd = "".join(sorted(s))
            if srtd not in m:
                m[srtd]=[]
            m[srtd].append(s)
        
        for l in m:
            res.append(m[l])

        return res

            





            

        