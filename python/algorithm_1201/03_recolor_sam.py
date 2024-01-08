class Solution:
    def minimum_recolors(self, blocks: str, k: int) -> int:
        min_count = blocks.count('W')
        for i in range(len(blocks)-k+1):
            new_count = blocks[i:i+k].count('W')
            min_count = min(min_count, new_count)
        return min_count

sol = Solution()
print(sol.minimum_recolors('WBBWBBWBW', 7))