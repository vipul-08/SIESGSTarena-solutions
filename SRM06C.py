def swapPositions(list, pos1, pos2): # Swapping algo
      
    list[pos1], list[pos2] = list[pos2], list[pos1] 
    return list

u = int(input())
for o in range(u):
    count = 0
    left = []
    right = []
    a = int(input())
    intercept = [0 for i in range(a)]

    for i in range(a):  # 2 Lists for Input
        x,y = list(map(int,input().split()))
        left.append(x)
        right.append(y)

    for i in range(a-1): # Sorting right, and swapping left similarly
        for j in range(a-1):
            if right[j] > right[j+1]:
                swapPositions(left, j, j+1)
                swapPositions(right, j, j+1)

    for i in range(a): # Main Algo
        if intercept[i] == 0:
            j = i+1
            while j < a:
                if left[j] <= right[i]:
                    intercept[j] = 1
                j = j+1
            intercept[i] = 1
            count = count+1
    print(count)