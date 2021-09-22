#Link to Contest https://www.codechef.com/START12C/problems/

#Question 1

'''for _ in range(int(input())):
    x=map(int,input().split())
    sum_one,sum_zero=0,0
    for i in x:
        if i==1:
            sum_one+=1
        else:
            sum_zero+=1
    if sum_one>sum_zero:
        print("Yes")
    else:
        print("No")'''

#Question 02

'''from time import time
x=time()
for _ in range(int(input())):
    n=int(input())
    for i in range(10**(n-1),10**(n+1)):
        if i%3==0 and i%9!=0 and i%2==1:
            print(i)
            print(time()-x)
            break'''

#Question 03

for _ in range(int(input())):
    a,b,c=map(int,input().split())
    x,y,z=map(int,input().split())
    