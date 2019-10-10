def small(a,n) :
    k=int(input("enter"))
    for i in range(n) :
        for j in range(n-1) :
            if a[j]>a[j+1] :
                c=a[j]
                a[j]=a[j+1]
                a[j+1]=c
    print(a[k-1])
n=int(input())
a=list(map(int,input().split()))
small(a,n)