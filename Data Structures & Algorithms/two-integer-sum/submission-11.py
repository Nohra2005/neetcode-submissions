class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = {}
        for i in range(len(nums)):
            if nums[i] in hashtable:
                hashtable[nums[i]].append(i)
            else:
                hashtable[nums[i]] = [i]
        for x in hashtable:
            n = target - x
            if n in hashtable:
                if n == x:
                    if len(hashtable[x]) <2:
                        continue
                    else:
                        i = hashtable[x][0]
                        j = hashtable[x][1]
                else:
                    i = hashtable[x][0]
                    j = hashtable[n][0]
                listoutput = [i,j]
                return listoutput
