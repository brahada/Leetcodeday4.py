class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack=[]
        n=k
        for cur in num:
            while k and stack and stack[-1]>cur:
                stack.pop()
                k=k-1
            stack.append(cur)
        ans="".join(stack[0:len(num)-n]).lstrip("0")
        if len(ans):
            return ans
        else:
            return "0"
