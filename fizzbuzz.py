# 3. 
# Написати fizzbuzz для 20 комплектів по три числа, які записані в файл. 


file = open('numbers.txt','r')
for line in file:
    fizz,buzz,n = list(map(int,line.split()))
    print('fizz = ', fizz, 'buzz = ', buzz, 'n = ', n)
    for x in range(1,n+1):
        if x % fizz == 0 and x % buzz == 0:
            print('FB ', end='')
        elif x % fizz == 0:
            print('F ', end='')
        elif x % buzz == 0:
            print('B ', end='')
        else:
            print(x,' ', end='')
    print()
    print('------------------------------')
        
file.close()


