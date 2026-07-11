class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashtable = {}
        max_length = 0
        start = 0
        for i in range(len(s)) :
            if s[i] in hashtable and hashtable[s[i]]>=start:
                start = hashtable[s[i]] + 1
            max_length = max(max_length, i - start + 1)
            hashtable[s[i]] = i
        max_length = max(max_length, len(s) - start)
        return max_length