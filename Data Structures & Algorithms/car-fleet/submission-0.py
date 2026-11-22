
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Only compare if the position is fronter
        stack = []
        for i in range (len(position)):
            #position, time
            time = (target - position[i]) /speed[i]
            stack.append([position[i],time])
        sorted_list = sorted(stack, key = lambda x:x[0])
        result = 0
        while sorted_list:
            a = sorted_list.pop()
            time = a[1]
            while sorted_list and sorted_list[-1][1] <= time:
                sorted_list.pop()
            result += 1
        return result


                
                
        