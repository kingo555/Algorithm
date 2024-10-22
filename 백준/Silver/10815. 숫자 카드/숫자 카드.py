import sys

n = int(sys.stdin.readline().rstrip())
cards = list(map(int,sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline().rstrip())
m_list = list(map(int,sys.stdin.readline().rstrip().split()))

cards.sort()
answer=[]

def bs(data, target) :
    start = 0
    end = len(data)-1

    while start <= end :
        mid = (start+end)//2

        if data[mid]== target :
            return True
        elif data[mid] < target :
            start = mid +1
        elif data[mid] > target :
            end = mid-1
    return False

for i in m_list :
    if bs(cards,i) :
        print(1,end=' ')
    else :
        print(0, end=' ')