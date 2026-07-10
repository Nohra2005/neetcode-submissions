class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for i in range(len(strs)):
            s = strs[i]
            key = "".join(sorted(s))
            if key in groups:
                groups[key].append(strs[i])
            else:
                groups[key] = [strs[i]]
        return list(groups.values())