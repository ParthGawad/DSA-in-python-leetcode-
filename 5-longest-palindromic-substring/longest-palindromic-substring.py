class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        reslen = 0
        s_len = len(s)

        for i in range(s_len) : 
            # odd length
            l,r = i,i
            while l >= 0 and r < s_len and s[l] == s[r] :
                if (r - l + 1) > reslen : 
                    res = s[l:r+1] 
                    reslen = r - l + 1
                l -= 1
                r += 1
            
            # even length 
            l,r = i,i+1
            while l >= 0 and r < s_len and s[l] == s[r] :
                if (r - l + 1) > reslen : 
                    res = s[l:r+1] 
                    reslen = r - l + 1
                l -= 1
                r += 1

        return res