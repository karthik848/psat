def ins(a,n) :
    b=int(input("enter the no."))
    if b<a[0] :
        pos=0
    elif b>a[n-1] :
        pos=n
    else :
        for i in range(n-1) :
            if b>a[i] and b<a[i+1] :
                pos=i+1
    for i in range(n-1,pos,-1) :
        a[i]=a[i-1]
    a[pos]=b
    print(" # NEW # ")
    for i in range(n) :
        print(a[i])
    return
n=int(input())
arr=list(map(int,input().split()))
ins(arr,n)
