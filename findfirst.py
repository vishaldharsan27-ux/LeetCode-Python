class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        r=""
        for i in words:
            if i==i[::-1]:
                r+=i
                return r
        return r
