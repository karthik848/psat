def merge(a,b,m,n) :
    a.sort()
    b.sort()
    c=[]
    for i in range(m+n+1) :
        if a[i]<b[i] :
            c[i]=a[i]
        elif a[i]>b[i] :
            c[i]=b[i]
        elif a[i]==b[i] :
            c[i]=a[i]
    for k in range(i,m) :
        c[k]=a[k]
    for k in range(i,n) :
        c[k]=b[k]
    return
m=int(input())
n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
merge(a,b,m,n)



