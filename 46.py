def search(a) :
    x=int(input("enter the no"))
    for i in a :
        if x==i :
            print("Found")
    return
n=int(input())
a=list(map(int,input().split()))
search(a)
