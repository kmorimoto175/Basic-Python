a, b, c = map(int, input().split())

t = a
x = 0
while t <= b:
 if c % t == 0:
  x += 1
  t += 1
 else:
  t += 1
print(x)
