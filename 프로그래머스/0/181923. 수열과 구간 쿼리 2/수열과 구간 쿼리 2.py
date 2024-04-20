def solution(arr, queries):
    result= []
    temp = []
    
    for s,e,k in queries :
        temp = list(filter(lambda x:x>k, sorted(arr[s:e+1]))) # 범위중 k보다 큰거 temp로
        if len(temp) > 0: #k보다큰것
            result.append(temp[0]) # 그중 작은것
        else :
            result.append(-1)
    return result