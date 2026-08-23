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

def minimumSwaps(arr):
    swaps = 0
    i = 0
    
    while i < len(arr):
        correct_index = arr[i] - 1
        
        if arr[i] != i + 1:
            arr[i], arr[correct_index] = arr[correct_index], arr[i]
            swaps += 1
        else:
            i += 1
            
    return swaps

def minimumBribes(q):
    bribes = 0

    for i in range(len(q)):
        if q[i] - (i + 1) > 2:
            print("Too chaotic")
            return

        for j in range(max(0, q[i] - 2), i):
            if q[j] > q[i]:
                bribes += 1

    print(bribes)
    
def sherlockAndAnagrams(s):
    count = 0

    for length in range(1, len(s)):
        seen = {}

        for i in range(len(s) - length + 1):
            substring = s[i:i + length]

            # Anagrams have the same sorted characters
            key = ''.join(sorted(substring))

            if key in seen:
                count += seen[key]
                seen[key] += 1
            else:
                seen[key] = 1

    return count