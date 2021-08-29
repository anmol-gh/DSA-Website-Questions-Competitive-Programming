# Link to question https://www.hackerrank.com/challenges/designer-door-mat/problem

# Solution

n, m = list(map(int, input().split()))

for i in range(0, int((n-1)/2)):
    s = ""
    s += '-'*int(int((m-1/2))/2)-i
    print(s)
