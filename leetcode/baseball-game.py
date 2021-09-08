#Link to Question https://leetcode.com/problems/baseball-game/
class Solution:
    def calPoint(self,ops):
        answer=[]
        result=0
        for i in ops:
            if i=="+":
                answer.append(answer[-2]+answer[-1])
                result+=answer[-1]
            elif i=="C":
                result-=answer[-1]
                del answer[-1]
            elif i=="D":
                answer.append(2*answer[-1])
                result+=answer[-1]
            else:
                answer.append(int(i))
                result+=answer[-1]
        return result

a=Solution()
a.calPoint(["5","2","C","D","+"])
a.calPoint(["5","-2","4","C","D","9","+","+"])
