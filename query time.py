query=int(input())
start=list(map(int,input().split()))
end=list(map(int,input().split()))
c=0
n=len(start)
for i in range(n):
    if query>=start[i] and query<=end[i]:
        c+=1
print(c)        
