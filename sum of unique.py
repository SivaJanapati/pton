data=list(map(int,input().split()))
dic={}
for i in data:
    if i not in dic.keys():
        dic[i]=1
    else:
        dic[i]+=1
s=0
for k,v in dic.items():
    if v==1:
        s+=k
print(s)
