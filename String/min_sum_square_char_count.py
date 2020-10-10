import heapq
def solve(inp,k):
    MAX_CHAR=26
    freq = [0]*MAX_CHAR
    for i in inp:
        freq[ord(i)-ord('a')]=freq[ord(i)-ord('a')]-1
    
    heapq.heapify(freq)
    while k:
        num = heapq.heappop(freq)
        num=num+1
        heapq.heappush(freq,num)
        k=k-1

    ans=0
    for i in range(0,MAX_CHAR):
        ans=ans+freq[i]*freq[i]
    return ans

print(solve("abbccc",2))
print(solve("aaab",2))
