def solution(arr, queries):
    temp = 0
    for i in range(len(queries)) :
        temp=arr[queries[i][0]]
        arr[queries[i][0]] = arr[queries[i][1]]
        
        arr[queries[i][1]] = temp

    
    return arr
        
