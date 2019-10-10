def rotate(a,n) :
    for i in range(n) :
        s=a[i]
        a[i]=a[n-1]
        a[n-1]=s
    print(a)
    return
n=int(input())
a=list(map(int,input().split()))
rotate(a,n)
