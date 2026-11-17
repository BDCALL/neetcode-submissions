class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            n = len(s)
            result += str(n)
            result += "#"
            result += s 
        return result
        

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s): # 2#we
            j = i
            while s[j] != "#":
                j += 1
            num = int(s[i : j])
            string = s[j + 1 : j+ 1+num]
            result.append(string)
            i = j +num +1
        return result


