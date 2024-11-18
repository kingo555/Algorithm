import sys

n = int(sys.stdin.readline().rstrip())
cnt=n

for _ in range(n) :
    word=sys.stdin.readline().rstrip()
    for i in range(0,len(word)-1 ) :
        if word[i] == word[i+1] :
            pass
        elif word[i] in word[i+1 :] :
            cnt -= 1
            break

print(cnt)