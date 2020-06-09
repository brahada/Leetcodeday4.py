class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        kad=self.kadane(A)
        wrap=0
        n=len(A)
        for i in range(n):
            wrap+=A[i]
            A[i]=-A[i]
        wrap=wrap+self.kadane(A)
        if wrap>kad and wrap!=0:
            return wrap
        else:
            return kad
            
    def kadane(self,nums):
        maxs,curs=nums[0],nums[0]
        for n in nums[1:]:
            curs=max(n,curs+n)
            maxs=max(curs,maxs)
        return maxs
