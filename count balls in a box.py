low=int(input())
high=int(input())
dic={}
s=0
for i in range(low,high+1):
    s=0
    while(i):
        r=i%10
        i=i//10
        s=s+r
    if s not in dic.keys():
        dic[s]=1
    else:
        dic[s]+=1
print(dic)        
print(max(dic.values()))
