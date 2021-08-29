#Question 01

'''for _ in range(int(input())):
    array=list(map(int,input().split()))
    sum_team_one=0
    sum_team_two=0
    for i in range(len(array)):
        if i%2==0:
            sum_team_one+=array[i]
        else:
            sum_team_two+=array[i]
    if sum_team_two>sum_team_one:
        print(2)
    elif sum_team_one>sum_team_two:
        print(1)
    else:
        print(0)'''

for _ in range(int(input())):
    n,m,x=list(map(int,input()))
    arr=list(map(int,input().split()))