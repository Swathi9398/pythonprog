a = int(input())
b = int(input())
c = int(input())
if a==b:
  print("a == b")
if a==c:
  print("a==c")
if b==c:
  print("b == c")
if a>b and b>c:
  print("a")
elif b>c:
  print("b")
else:
  print("c")
