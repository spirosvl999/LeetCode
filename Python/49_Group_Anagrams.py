class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for s in strs:            
            count = [0] * 26

            for c in s:
                count[ord(c) - ord("a")] +=1                 # ASCII Value - ASCII value of A so we get the right number on the table
            
            key = tuple(count)
            
            if key in res:
                res[key].append(s)
            else:
                res[key] = [s]
                                                                              # RunTime: 20 ms // Beats 25.58%
        return list(res.values())                                             # Memory: 22.50 MB // Beats 31.90%
