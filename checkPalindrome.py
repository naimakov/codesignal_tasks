def solution(inputString):
    for i in range(0, len(inputString)//2):
        if inputString[i] != inputString[len(inputString)-1-i]:
            return False
    return True
