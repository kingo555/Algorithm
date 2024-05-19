def solution(arr):
    count = 0
    while True :
        arr2 = []
        for i in arr :
            if i>=50 and i%2==0 :
                arr2.append(int(i/2))
            elif i< 50 and i%2 ==1 :
                arr2.append(i*2+1)
            else :
                arr2.append(i)
        if arr== arr2 :
            return count
        else :
            count +=1
            arr= arr2
            