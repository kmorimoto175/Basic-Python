a, b, c = map(int, input().split())
d = min(a,b,c)
e = max(a,b,c)
if d < a and a < e:
 f = a
elif d < b and b < e:
 f = b
else :
 f = c
print(str(d) + " "+ str(f) + " " + str(e))
