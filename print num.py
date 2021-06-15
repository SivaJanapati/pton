
n = int(input())
num=0
for i in range(1,n+1):
    t=i
    c=0
    while i:
        r=i%10
        i=i//10
        c+=1
    num=(num*(10**c))+t    
print(num)
