class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = ""
        for i in range(len(s)):
            try:
                num = int(s[i])
                st += s[i]
            except:
                if ord(s[i].lower())>=ord('a') and ord(s[i].lower())<=ord('z'):
                    st+=s[i].lower()
        start = 0
        end = len(st)-1
        while start<=end:
            if st[start]!=st[end]:
                return False
            else:
                start+=1
                end-=1
        return True