data=list(map(int,input().split()))
n=len(data)
res=[0 for i in range(n)]
e=0
o=n-1
for i in data:
    if i%2:
        res[o]=i
        o-=1
    else:
        res[e]=i
        e+=1
print(res)        
    
