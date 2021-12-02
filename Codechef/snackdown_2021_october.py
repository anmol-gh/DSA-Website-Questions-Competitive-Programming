#Link to Contest
# https://www.codechef.com/SNCKQL21

#Question 1

for _ in range(int(input())):
    a,b,c=map(int,input().split())
    if a==7 or b==7 or c==7:
        print("YES")
    else:
        print("NO")


#Question 2

for _ in range(int(input())):
    t=list(map(int,input().split()))
    india,england=0,0
    for i in t:
        if i==1:
            india+=1
        elif i==2:
            england+=1
            