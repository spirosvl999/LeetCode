class Solution(object):
    def maximumWealth(self, accounts):
        max_w = -1

        for i in range(len(accounts)):
            person = sum(accounts[i])
            max_w = max(max_w, person)
        
        return max_w
