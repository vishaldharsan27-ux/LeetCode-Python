class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        arr = strs

        prefix = arr[0]

        for s in arr[1:]:
            while s[:len(prefix)] != prefix:
                prefix = prefix[:-1]

        return prefix