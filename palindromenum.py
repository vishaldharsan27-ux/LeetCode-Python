class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        else:
            t=str(x)
            if t==t[::-1]:
                return True
            else:
                return False