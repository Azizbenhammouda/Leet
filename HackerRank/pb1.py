from collections import Counter

def sockMerchant(n, ar):
    counts = Counter(ar)
    pairs = 0
    
    for count in counts.values():
        pairs += count // 2  
        
    return pairs

def checkMagazine(magazine, note):
    magazine_count = Counter(magazine)

    for word in note:
        if magazine_count[word] == 0:
            print("No")
            return

        magazine_count[word] -= 1

    print("Yes")

def twoStrings(s1, s2):
    dic1 = Counter(s1)
    for letter in s2:
        if dic1[letter] != 0:
            return "YES"
    return "NO"