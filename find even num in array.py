#def count(num):
#    c=0
#    while num:
#        num=num//10
#        c+=1
#    return c       
#def findnum(n,data):
#    c=0
#    for i in data:
#        if count(i)%2==0:
#            print(i)
#            c+=1
#    return c        
#n=int(input())
#data=list(map(int,input().split()))
#print(findnum(n,data))


def findnum(n,data):
    c=0
    for i in data:
        if len(str(i))%2==0:
            c+=1
    return c        
n=int(input())
data=list(map(int,input().split()))
print(findnum(n,data))
