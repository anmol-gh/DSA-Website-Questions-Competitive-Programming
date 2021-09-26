#Link to Contest

#Question 01
'''for _ in range(int(input())):
    m,n,k=map(int,input().split())
    res=m-(n*k)
    if res<=0:
        print('NO')
    else:
        print('YES')'''

#Question 02

'''for _ in range(int(input())):
    n,p,x,y=map(int,input().split())
    arr=list(map(int,input().split()))
    result=0
    for i in range(0,p):
        if arr[i]==0:
            result+=x
        else:
            result+=y
    print(result)
'''

#Question 03 -> Incomplete

'''for _ in range(int(input())):
    P,a,b,c,x,y=map(int,input().split())
    '''

#Question 04 -> Partially Correct

'''for _ in range(int(input())):
    array=list(map(int,input()))
    replaced=[]
    present=array
    length=len(array)
    position=0
    result=0
    for i in range(length):
        if array[i]==0:
            replaced.append(1)
        else:
            replaced.append(0)
    while position!=length:
        if present[position]==0:
            if present==replaced:
                present=array
            else:
                present=replaced
            result+=1
            position+=1
        else:
            position+=1
    print(result)'''

#Question 05 -> Incorrect
def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

for _ in range(int(input())):
    a,b=map(int,input().split())
    prime_a=prime_factors(a)
    prime_b=prime_factors(b)
    print(prime_a,prime_b)