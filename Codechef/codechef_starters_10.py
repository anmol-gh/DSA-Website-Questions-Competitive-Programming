#Question 01

'''
for _ in range(int(input())):
    a,b,c=list(map(int,input().split()))
    if c<b and c<a:
        print("Alice")
    elif b<c and b<a:
        print("Bob")
    else:
        print("Draw")
'''

#Question 02
for _ in range(int(input())):
    n,k,s=list(map(int,input().split()))
    #arr=n+k-1
    non_rep_sun=n*n
