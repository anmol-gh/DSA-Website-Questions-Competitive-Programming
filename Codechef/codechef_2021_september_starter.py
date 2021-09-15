'''Link to contest 
https://www.codechef.com/START11C/problems'''

#Question 01
'''for _ in range(int(input())):
    x=["North","East","South","West"]
    seconds=int(input())
    print(x[seconds%4])'''

#Question 02

for _ in range(int(input())):
    n,s=(map(int,input().split()))
    if n>=s:
        print(n)
    elif n<s:
        print(s-n)
    else:
        print()