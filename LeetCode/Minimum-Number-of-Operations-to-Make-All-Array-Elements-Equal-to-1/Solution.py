int cnt1 = 0;
for (int i = 0; i < n; ++i)
    cnt1 += (nums[i] == 1);
if (cnt1)
    return n - cnt1;