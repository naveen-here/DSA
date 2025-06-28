maxSubsequence = (nums, k) => [...nums.entries()]
    .sort((a, b) => b[1] - a[1])
    .slice(0, k)
    .sort((a, b) => a[0] - b[0])
    .map(([i, v]) => v)