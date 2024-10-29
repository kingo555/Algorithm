import sys

n = int(sys.stdin.readline().rstrip())
num_list=[]

for _ in range(n) :
    num_list.append(int(sys.stdin.readline().rstrip()))

num_list.sort()

print(round(sum(num_list)/n))
print(num_list[n//2])

freq={}
max_freq_lst=[]
for i in num_list :
    if i not in freq :
        freq[i] = 1
    else :
        freq[i] += 1

max_freq = max(freq.values())

for j in freq :
    if freq[j] == max_freq :
        max_freq_lst.append(j)

if len(max_freq_lst) <= 1 :
    print(max_freq_lst[0])
else :
    print(max_freq_lst[1])

print(num_list[-1]- num_list[0])