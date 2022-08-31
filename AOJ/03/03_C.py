list = []
while True:
 a, b = map(int,input().split())
 if (a, b) == (0, 0):
  break
 else:
  list.append([a, b])
for i in list:
 i.sort()
 print(*i)

