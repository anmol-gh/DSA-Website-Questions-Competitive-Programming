n, m = list(map(int, input().split()))
arr = set(map(int, input().split()))
happiness = list(map(int, input().split()))
unhappy = list(map(int, input().split()))
answer = 0

for i in range(len(happiness)):
    khush = happiness[i]
    dard = unhappy[i]
    khush_visited = False
    dard_visited = False
    for j in arr:
        if khush_visited == True and dard_visited == True:
            break
        elif khush == j and khush_visited == False:
            answer += 1
            khush_visited = True
        elif dard == j and dard_visited == False:
            answer -= 1
            dard_visited = False
print(answer)


