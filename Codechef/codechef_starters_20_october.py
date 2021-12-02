#Link to Contest https://www.codechef.com/START16C?order=desc&sortBy=successful_submissions
#Question 01
for _ in range(int(input())):
    n,x,p=map(int,input().split())
    if (x*3)-(n-x)>=p:
        print("PASS")
    else:
        print("FAIL")

#Question 02

for _ in range(int(input())):
    x,y=map(int,input().split())
    s=input()
    work=0
    gap=0
    for i in s:
        if i==1:
            work+=1
    total=work*6+gap*3