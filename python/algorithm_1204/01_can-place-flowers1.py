class Solution:
    def can_place_flowers(self, flowerbed: list[int], n: int) -> bool:
        # 1) for enumerate 사용해 반복 (인덱스 : i, 값: plant)
        for i, plant in enumerate(flowerbed):
            # 2) 만약 꽃이 심어져있으면 (plant 값이 1)
            if plant == 1:
            #   3) 다음으로 넘어간다.
                continue
            # 4) 만약 화단의 위치(i)가 0보다는 크고(and), 앞에 꽃(flowerbed[i-1] == 1)이 심어져있으면, 
            if i > 0 and flowerbed[i-1] == 1:
            #   3) 다음으로 넘어간다.
                continue            
            # 5) 만약 화단의 위치(i)가 화단 길이(len(flowerbeb)-1)보다는 작고,
            # 뒤에 꽃(flowerbed[i+1] == 1)이 심어져있으면,
            if i < len(flowerbed) - 1  and flowerbed[i+1] == 1 :
            #   3) 다음으로 넘어간다.
                continue
            # 꽃 심고 n에서 1 감소
            # 1) flowerbed[i] 값을 1로 바꾼다.
            flowerbed[i] = 1
            # 2) n이 1 감소된다.
            n -= 1
        print(flowerbed, n)
        return n <= 0
        
        
sol = Solution()
result = sol.can_place_flowers([1,0,0,0,0,1], 2)
print(result)