class Solution:
    def isPowerOfTwo(self,n): 
        if n:
            return not n&n-1
        else:
            return False
