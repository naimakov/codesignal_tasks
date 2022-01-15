def solution(inputArray):
    max = -1000000
    for i in range(1,len(inputArray)) :
        if (max < inputArray[i-1]*inputArray[i]) :
            max = inputArray[i-1]*inputArray[i]
    return max
