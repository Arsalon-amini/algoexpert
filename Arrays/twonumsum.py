# write a fn takes in array of distinct ints and int rep a target sum
# if any two nums in array sum to target, return in array, any order

# O(n^2) time | O(n) space
def twonNumSum_worst(array, target):
    for i in range(len(array) - 1):
        firstNum = array[i]
        for j in range(i+1, len(array)):
            secondNum = array[j]
            if firstNum + secondNum == target:
                return [firstNum, secondNum]


# O (n logn) time, o(1) space
def twoNum_best(array, targetSum):
    array.sort()

    left_idx = len(array) - 1
    right_idx = 0

    for i in range(len(array)):
        firstNum = array[left_idx]
        secondNum = array[right_idx]
        currentSum = firstNum + secondNum

        if currentSum < targetSum:
            right_idx += 1
        elif currentSum > targetSum:
            left_idx -= 1
        else:
            return [firstNum, secondNum]
