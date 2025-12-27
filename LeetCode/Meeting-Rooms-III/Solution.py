1class Solution:
2    def mostBooked(self, n: int, meetings: list[list[int]]) -> int:
3        meetings.sort()
4
5        count = [0] * n
6        timer = [0] * n
7
8        itr = 0
9
10        while itr < len(meetings):
11            start, end = meetings[itr]
12            dur = end - start
13
14            room = -1
15            earliest = 10**18
16            earliestRoom = -1
17
18            for i in range(n):
19                if timer[i] < earliest:
20                    earliest = timer[i]
21                    earliestRoom = i
22                if timer[i] <= start:
23                    room = i
24                    break
25
26            if room != -1:
27                timer[room] = end
28                count[room] += 1
29            else:
30                timer[earliestRoom] += dur
31                count[earliestRoom] += 1
32
33            itr += 1
34
35        maxv = 0
36        idx = 0
37        for i in range(n):
38            if count[i] > maxv:
39                maxv = count[i]
40                idx = i
41
42        return idx