class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        mymap = {}
        n = len(s)
        out = 0
        left = 0
        right = 0
        for right in range(n):
            ch = s[right]
            if ch in mymap and mymap[ch] >= left:
                left = mymap[ch] + 1
            else:
                out = max(out, right - left + 1)
            mymap[ch] = right
        return out