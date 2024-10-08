n = int(input())
charDic = {} # 알파벳과 가중치를 key, value로 저장

for _ in range(n) :
  temp = list(input())

  for i in range(len(temp)-1,-1,-1) :
    char = temp[len(temp)-1-i]
    if char in charDic :
      charDic[char] += 10 ** i #알파벳이 있으면 해당 자릿수 * 알파벳 더해주기
    else :
      charDic[char] = 10 ** i # 알파벳이 없으면 새로 지정

charDic = dict(sorted(charDic.items(), key=lambda x : x[1], reverse=True))
# charDic의 항목들을 가중치 순으로 내림차순 정렬
charNum = 9
result = 0

for j in charDic :
  result += charDic[j] * charNum
  charNum-=1
print(result)