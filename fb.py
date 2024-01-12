f = int(input())
b = int(input())
n = int(input())

print(f,b,n)

for x in range(1,n+1):
   if not x%f and not x%b:
      print("FB", end = " ")
   elif not x%f:
      print("F", end = " ")
   elif not x%b:
      print("B", end = " ")
   else:
      print(x, end = " ")


