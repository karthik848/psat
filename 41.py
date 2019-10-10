def m(arr,n) :
    max=0
    for i in range(n) :
        if max<arr[i] :
            max=arr[i]
    print(max)
    return
n=int(input())
a=list(map(int,input().split()))
m(a,n)

