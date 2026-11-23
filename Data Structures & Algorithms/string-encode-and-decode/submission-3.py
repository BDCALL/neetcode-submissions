class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s))
            encoded += "#"
            encoded += s
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            start = i
            while s[start]!= "#":
                start += 1
            num = int(s[i:start])
            string = s[start+1: start +1 + num]
            decoded.append(string)
            i = start + 1 + num 
        return decoded