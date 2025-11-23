static int f(int i, int mod, vector<int>& nums){
    if (i<0) return mod==0? 0:-1e9; // base case
    if (dp[i][mod]!=-1) return dp[i][mod];// avoid of redudancy

    const int x=nums[i];
    // modPrev= (mod-x) mod 3
    int modPrev=mod-x%3; modPrev+=(-(modPrev<0)) & 3;

    int take=x+f(i-1, modPrev, nums);// take
    int skip=f(i-1, mod, nums); // skip

    return dp[i][mod]=max(take, skip);// store to dp
}