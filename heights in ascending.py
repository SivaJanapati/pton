#heights=list(map(int,input().split()))
#d=sorted(heights)
#n=len(d)
#c=0
#for i in range(n):
#    if d[i]!=heights[i]:
#        c+=1
#print(c)        

data=list(map(int,input().split()))
n=len(data)
c=0
for i in data:
    if i<=(i+1) and (i+1)==min(data(i+1,n+1)):
        c=0
    else:
        c+=1
print(c)        
        
                               
                               
                               
                               
