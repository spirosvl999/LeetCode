class Solution(object):
    def longestCommonPrefix(self, strs):
        pref = ""
        for i in range(len(strs[0])):
            for word in strs:
                if i == len(word) or strs[0][i] != word[i]:
                    return pref
            pref = pref + strs[0][i]
        return pref
