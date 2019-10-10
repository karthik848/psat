def even(a,n,s=0) :
    for i in range(0,n,2) :
        s=s+a[i]
    print(s)
    return
n=int(input())
a=list(map(int,input().split()))
even(a,n)
