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
