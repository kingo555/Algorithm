import heapq
n = int(input())
plus = []
minus = []
answer = 0
# plus와 minus로 나눠서 계산

for _ in range(n) :
  a = int(input())
  if a == 1 : # 1일 경우에는 무조건 더하는 게 이득
    answer +=1
  elif a>0 : # 0일 경우에는 plus랑 곱하는 게 이득
    plus.append(a)
  else :
    minus.append(a)

plus.sort()
minus.sort(reverse=True)

while len(plus) != 0 : # plus는 높은 수끼리 곱하기
  if len(plus) ==1 :
    answer += plus.pop()
  else :
    answer += plus.pop() * plus.pop()

while len(minus) != 0 : # minus는 낮은 수끼리 곱하기
  if len(minus) == 1 :
    answer += minus.pop()
  else :
    answer += minus.pop() * minus.pop()

print(answer)
