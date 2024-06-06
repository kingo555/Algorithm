def solution(arr, flag):
    result = []
    for i,v in enumerate(flag) :
        if v :
            for j in range(0,arr[i]*2) :
                result.append(arr[i])
        else :
            for j in range(0, arr[i]) :
                result.pop();
            
    return result