class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ''
        if len(strs)>0:
            for i in range(len(strs)):
                s += str(len(strs[i]))+'#'+strs[i]
        return s

    def decode(self, s: str) -> List[str]:
        results = []
        if len(s)>0:
            curr  = 0
            while curr<len(s):
                word = ""
                number = ""
                while s[curr]!='#':
                    number += s[curr]
                    curr += 1
                number = int(number)
                curr += 1
                for i in range(curr, curr+number):
                    word+=s[curr]
                    curr += 1
                results.append(word)
        return results
