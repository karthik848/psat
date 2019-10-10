def s(a,n) :
    s=0
    for i in range(n) :
        if a[i]%2==0 :
            s=s+a[i]
    print(s)
    return
n=int(input())
a=list(map(int,input().split()))
s(a,n)
