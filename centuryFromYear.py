def solution(year):
    if year <= 100 :
        return 1
    else :
        return year // 100 if year % 100 == 0 else year // 100 + 1
