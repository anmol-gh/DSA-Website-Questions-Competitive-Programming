#Link to Contest

#Question 01
for i in range(int(input())):
    x, y, z = map(int, input().split())
    if y < x:
        print("Pizza")
    elif z < x:
        print("Burger")
    else:
        print("Nothing")

#Question 02

for i in range(int(input())):
    n, a = map(int, input().split())
    print(min(a, n - a))

#Question 03 incomplete
for i in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    maximum=0
    total=sum(arr)
    for j in range(n-1):
        x=total-arr[j]
