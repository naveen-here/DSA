1class Solution:
2    def removeDuplicateLetters(self, s: str) -> str:
3        last_occr = {}
4        stack = []
5        visited = set ()
6
7        for i in range (len(s)):
8            last_occr[s[i]] = i
9        for i in range (len(s)):
10            if s[i] not in visited :
11                while(stack and stack[-1] > s[i] and last_occr[stack[-1]] > i):
12                    visited.remove(stack.pop())
13                
14                stack.append(s[i])
15                visited.add(s[i])
16        return "" .join(stack)
17        