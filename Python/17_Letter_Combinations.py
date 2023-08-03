class Solution(object):
    def letterCombinations(self, digits):
        output = [""]
        dig_to_lett = { "2": "abc",                 # We let know
                        "3": "def",                 # what number is what letter.
                        "4": "ghi",
                        "5": "jkl",
                        "6":  "mno",
                        "7": "pqrs",
                        "8": "tuv",
                        "9": "wxyz"}

        if not digits:                              # If we have not digits we return []
            return                                  # and not [""]

        for i in digits:
            temp = []                               # We have to create a temp to get the number
            for j in dig_to_lett[i]:
                for k in output:
                    temp.append(k+j)
            output = temp
        return output
