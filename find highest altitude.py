#gain=list(map(int,input().split()))
#n=len(gain)
#data=[0 for i in range(n+1)]
#for i in range(n):
#    data[i+1]=data[i]+gain[i]
#a=max(data)
#print(a)

gain=list(map(int,input().split()))
data=0
d=0
for i in gain:
    d=d+i
    if data<d:
        data=d
reprint(data)        
