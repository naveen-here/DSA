class Solution(object):
    def twoSum(self, numbers, target):
        left = 0
        right = len(numbers) - 1;

        while (numbers[left] + numbers[right] != target):
            if(numbers[left] + numbers[right] < target) :
                left +=1
            else :
                right -=1
            
        return [left+1, right+1]  #problem needs 1 based indexing

        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        