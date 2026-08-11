
def charRep(s,k):
    def find(f):
        maxc=-1
        for i in range(256):
            maxc=max(maxc,f[i])
        return maxc
    low=0
    high=0
    res=float("-inf")
    f=[0]*256

    for high in range(len(s)):
        f[ord(s[high])]+=1
        maxVal=find(f)
        length=high-low+1
        diff=length-maxVal

        while(diff>k):
            f[ord(s[low])]-=1
            low+=1

            maxVal=find(f)
            length=high-low+1
            diff=length-maxVal

        length=high-low+1
        res=max(length,res)
    return res






s = "ABAB"
k = 2
print(charRep(s,k))
