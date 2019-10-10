def replace(a,n) :
    b=a
    for i in range(1,n) :
        b[i]=a[i+1]*a[i-1]
    b[0]=a[0]*a[1]
    b[n-1]=a[n-1]*a[n-2]
    print(b)
n=int(input())
a=list(map(int,input().split()))
replace(a,n)
