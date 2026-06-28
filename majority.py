class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            d[i]=d.get(i,0)+1
        m=max(d.values())
        for key,value in d.items():
            if value==m:
                return key
        
