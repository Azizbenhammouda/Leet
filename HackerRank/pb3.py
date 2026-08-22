def jumpingOnClouds(c):
    jumps = 0
    i = 0

    while i < len(c) - 1:
        if i + 2 < len(c) and c[i + 2] == 0:
            i += 2
        else:
            i += 1

        jumps += 1

    return jumps

def repeatedString(s, n):
    # Write your code here
    num=s.count("a")
    div=n // len(s)
    reste=n%len(s)
    result=num*div
    arr = s[:reste]
    count=arr.count("a")
    result+=count
    return result

def hourglassSum(arr):
    # Write your code here  
    smth=[]  
    for i in range(4):  
        for j in range(4):   
                smth.append(arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]) 

    return max(smth)

def rotLeft(a, d):
    result = [0] * len(a)

    for i in range(len(a)):
        result[(i - d) % len(a)] = a[i]

    return result