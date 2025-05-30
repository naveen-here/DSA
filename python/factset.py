
## Flatten N-Dimensional Array to 1D Array
def flatten_array(arr):
    result = []
    stack = arr[::-1]

    while stack:
        current = stack.pop()
        if isinstance(current, list):        #isinstance(value,type) check value == type true otherwise false
            stack.extend(current[::-1])
        else:
            result.append(current)
    return result


##Sum of Matrix Elements
def matrix_sum(matrix):
    sum = 0

    stack = matrix[ :]
    while stack:
        current = stack.pop()
        if isinstance(current,list):
            stack.extend(current)
        else :
            sum +=current
    return sum


###Triplet Counting

def count_triplets(nums, k):
    result = 0
    for i in range(len(nums)):    
        for j in range(i + 1, len(nums)):
            for x in range(j + 1, len(nums)):

                if (nums[i] + nums[j] + nums[x]) == k:
                    result += 1

    return result


