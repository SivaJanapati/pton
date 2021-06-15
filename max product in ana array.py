#n=int(input())
#data=list(map(int,input().split()))
#num=[]
#for i in range(0,n):
#    for j in range(1,n):
#       p=(data[i]-1)*(data[j]-1)
#       num.append(p)
#a=max(num)
#print(a)
    
n=int(input())
data=list(map(int,input().split()))
data.sort()
d=(data[-1]-1)*(data[-2]-1)
print(d)
