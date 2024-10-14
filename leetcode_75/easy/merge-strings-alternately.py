# Solution 1 intution + brute force
class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        maxl = len(word1) + len(word2)
        i1, i2 = 0, 0
        e1, e2 = len(word1), len(word2)
        bit = 1
        sol = ""
        print(maxl)
        for s in range(maxl):
            if (bit) and (i1 < e1):
                sol += word1[i1]
                i1 += 1
                bit = 0
            elif (not bit) and (i2 < e2):
                sol += word2[i2]
                i2 += 1
                bit = 1
            if (i1 == e1): bit = 0
            if (i2 == e2): bit = 1
        return sol
    
# Solution 2 optimized solution 
class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        l1 = len(word1)
        l2 = len(word2)
        i = 0
        sol = ""
        while (i < l1 or i < l2):
            if (i < l1):
                sol += word1[i]
            if (i < l2):
                sol += word2[i]
            i += 1
        return sol