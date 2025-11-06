#Dont copy this one, it will throw TLE, It is just for Understanding
def findXSum(nums, k, x):
    n = len(nums)
    ans = []
    for i in range(n - k + 1):
        window = nums[i:i+k]
        freq = Counter(window)
        top = sorted(freq.items(), key=lambda p: (p[1], p[0]), reverse=True)[:x]
        keep = set(v for v, _ in top)
        ans.append(sum(num for num in window if num in keep))
    return ans