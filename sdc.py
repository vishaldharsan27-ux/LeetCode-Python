class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        pos = []

        for i in range(len(s)):
            if s[i] == c:
                pos.append(i)

        ans = []
        j = 0

        for i in range(len(s)):
            while j + 1 < len(pos) and abs(pos[j + 1] - i) < abs(pos[j] - i):
                j += 1

            ans.append(abs(pos[j] - i))

        return ans