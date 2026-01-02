func repeatedNTimes(nums []int) int {
	n := len(nums)
    for i := range n - 2 {
        if nums[i] == nums[i+1] || nums[i] == nums[i+2] { return nums[i] }
    }
	return nums[n-1]
}