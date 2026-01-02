1class Solution:
2    def latestDayToCross(self, row: int, col: int, cells: list[list[int]]) -> int:
3        dsu = DSU(row * col + 2)
4        grid = [[0] * col for _ in range(row)]
5        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
6
7        for i in range(row * col):
8            r = cells[i][0] - 1
9            c = cells[i][1] - 1
10            grid[r][c] = 1
11
12            id1 = r * col + c + 1
13            for dr, dc in dirs:
14                nr, nc = r + dr, c + dc
15                if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 1:
16                    id2 = nr * col + nc + 1
17                    dsu.union(id1, id2)
18
19            if c == 0:
20                dsu.union(0, id1)
21            if c == col - 1:
22                dsu.union(row * col + 1, id1)
23
24            if dsu.find(0) == dsu.find(row * col + 1):
25                return i
26        return -1
27
28
29class DSU:
30    def __init__(self, n):
31        self.root = list(range(n))
32        self.size = [1] * n
33
34    def find(self, x):
35        if self.root[x] != x:
36            self.root[x] = self.find(self.root[x])
37        return self.root[x]
38
39    def union(self, x, y):
40        rx = self.find(x)
41        ry = self.find(y)
42        if rx == ry:
43            return
44        if self.size[rx] > self.size[ry]:
45            rx, ry = ry, rx
46        self.root[rx] = ry
47        self.size[ry] += self.size[rx]
48