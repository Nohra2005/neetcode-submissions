class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashtable = {}
        for i in range(len(nums)):
            if nums[i] not in hashtable:
                hashtable[nums[i]] = 1
        max_sequence = 0
        for i in range(len(nums)):
            start = nums[i]
            sequence = 1
            flag = True
            while flag:
                start +=1
                if start in hashtable:
                    sequence+=1
                else:
                    if sequence>max_sequence:
                        max_sequence = sequence
                    flag = False
        return max_sequence