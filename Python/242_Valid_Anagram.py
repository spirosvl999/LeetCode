class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range (len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)                          # The logic behind this one is 
            countT[t[i]] = 1 + countT.get(t[i], 0)                          # that we check how many we have for each letter
        for j in countS:                                                    # and we have to have the same amount on every letter.
            if countS[j] != countT.get(j, 0):                               # Runtime 15ms & Memory 17.92MB
                return False                                                # complexity unknown lol

        return True
