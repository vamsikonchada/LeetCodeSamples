class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        """
        y = str(x)
        n = len(y)
        for i in range(int(n/2)):
            if i >= (n-i-1):
                return True
            if y[i] != y[n-i-1]:
                return False
        return True
        """
        if x < 0:
            return False
        reverse = 0
        y = x
        while y != 0:
            mod = y % 10 
            reverse = (reverse * 10 ) + mod
            y = y/10
        return reverse == x