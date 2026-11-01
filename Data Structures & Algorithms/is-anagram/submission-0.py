class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False

        dict1={}

        for i in s:
            dict1[i]=1+dict1.get(i, 0)

        for j in t:
            if j not in dict1:
                return False
            dict1[j]-=1
            if dict1[j]<0:
                return False
        return True