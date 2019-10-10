def s(a,n) :
    for i in range(n) :
        for j in range(n-1) :
            if a[j]>a[j+1] :
                c=a[j]
                a[j]=a[j+1]
                a[j+1]=c
    print(a)
    return
n=int(input())
a=list(map(int,input().split()))
s(a,n)