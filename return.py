def sum(x):
	if x == 0:
	  return 0
    elif x == 1:
	  return 1
    else:
	  return x + sum(x-1)
y = sum(10)
print(y)