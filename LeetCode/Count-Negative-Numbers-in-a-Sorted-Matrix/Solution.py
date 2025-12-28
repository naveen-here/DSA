1class Solution:
2    def countNegatives(self, grid: List[List[int]]) -> int:
3        m = len(grid)
4        n = len(grid[0])
5
6        i = m - 1
7        j = 0
8        res = 0
9
10        while i >= 0 and j < n:
11            if grid[i][j] < 0:
12                res += n - j
13                i -= 1
14            else:
15                j += 1
16
17        return res
18