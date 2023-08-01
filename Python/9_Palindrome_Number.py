class Solution(object):
    def isPalindrome(self, x):
        number = str(x)
        if(number == number[::-1]):
            return True
        else:                                              # RunTime 12ms,
            return False                                   # Beating 99.99%  of Python Users.
