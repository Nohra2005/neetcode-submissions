class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numbers = {}
        for i in range(len(nums)):
            x = nums[i] 
            if x in numbers:
                numbers[x]+=1
            else:
                numbers[x] = 1
        result = []
        for key in numbers:
            result.append((key, numbers[key]))
        result.sort(key = lambda pair : pair[1], reverse = True)
        results = []
        for i in range(k):
            results.append(result[i][0])
        return results
           