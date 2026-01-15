1class Solution:
2    def maximizeSquareHoleArea(self, n: int, m: int, hBars: list[int], vBars: list[int]) -> int:
3        def maxSpan(bars: list[int]) -> int:
4            bars.sort()
5            res = 1
6            streak = 1
7            for i in range(1, len(bars)):
8                if bars[i] - bars[i - 1] == 1:
9                    streak += 1
10                else:
11                    streak = 1
12                res = max(res, streak)
13            return res + 1
14        
15        return min(maxSpan(hBars), maxSpan(vBars)) ** 2