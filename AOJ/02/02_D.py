W,H, x, y, r = map(int, input().split())
if r <= x and r <= y and W - x >= r and H - y >= r : 
 print("Yes")
else :
 print("No")
