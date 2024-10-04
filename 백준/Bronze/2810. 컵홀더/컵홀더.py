N = int(input())
seat = input()
Lcount = seat.count("LL")
Scount = seat.count("S")
holder_count = Lcount+Scount+1
if holder_count < N :
    print(holder_count)
else :
    print(N)
