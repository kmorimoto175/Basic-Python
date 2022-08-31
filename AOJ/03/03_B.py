a = []
while True:
 n = int(input())
 if n == 0:
  break
 else:
  a.append(n)
for i in range(len(a)):
 print(f"Case {i+1}: {a[i]}") 
