class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        i = 0
        result = []
        
        while i <= len(blocks) - k:
            window = blocks[i:k+i]
            result.append(window.count("W"))
            i += 1

        return min(result)
    
sol = Solution()
blocks = "WBBWWBBWBW"
k = 7
print(sol.minimumRecolors(blocks, k))