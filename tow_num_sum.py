# define the function that takes an array of ints ang a target number that is sum of two ints
def tow_num_sum(arr, target):
    # sort the array
    arr.sort()
    # we want to start from the beginning of the array and move towards the end
    leftindex = 0
    # we also want to determine where to stop
    rightindex = len(arr) - 1
    # start a while loop 
    while leftindex < rightindex:
        # we need to get a sum of each tow ints in the array moving right from index[0] and moving left from index[-1]
        # define a variable that holds this sums
        possibleSum = arr[leftindex] + arr[rightindex]
        # right Here if this possibleSum == our target, we want to return possibleSum
        if possibleSum == target:
            return [arr[leftindex], arr[rightindex]]
        # however; if possibleSum is less than our target, we move our left index by 1 to the right
        elif possibleSum < target:
            leftindex += 1
        # and if possibleSum is greater than target we move our right index by 1 to the left
        elif possibleSum > target:
            rightindex -= 1
    # if any of these conditions not met, just return an ampty array
    return []

# test our function
test1 = tow_num_sum([4, 5, 2, 0, 8, 7, 16], 13)
print(test1)