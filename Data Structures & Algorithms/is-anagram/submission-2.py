class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashtable = {}
        if len(s)!=len(t):
            return False
        for ch in s:
            if ch in hashtable:
                hashtable[ch]+=1
            else:
                hashtable[ch] = 1
        for ch in t:
            if ch in hashtable:
                if hashtable[ch] == 0:
                    return False
                else:
                    hashtable[ch] -= 1
            else:
                return False
        return True
