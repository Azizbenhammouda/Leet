from collections import Counter

def sockMerchant(n, ar):
    counts = Counter(ar)
    pairs = 0
    
    for count in counts.values():
        pairs += count // 2  
        
    return pairs