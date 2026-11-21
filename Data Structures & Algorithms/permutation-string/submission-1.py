class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        n = len(s1)
        l = 0
        array = [0] * 26
        array1 = [0] * 26
        for i in range (n):
            order = ord(s1[i]) - ord("a")
            order1 = ord(s2[i]) - ord("a")
            array[order] += 1
            array1[order1] += 1
        if array == array1:
            return True
        for j in range (n, len(s2)):
            order = ord(s2[j-n]) - ord("a")
            order1 = ord(s2[j]) - ord("a")
            array1[order] -= 1
            array1[order1] += 1
            if array == array1:
                return True
        return False

       

       

        