class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        s={}
        for i in nums:
            if i in s:
                s[i]+=1
            else:
                s[i]=1
        buckets=[]
        buckets=[[] for _ in range(len(nums)+1)]
        for i, freq in s.items():
            buckets[freq].append(i)
        result=[]
        for freq in range(len(nums),0,-1):
            for i in buckets[freq]:
                result.append(i)
                if len(result)==k:
                    return result
                