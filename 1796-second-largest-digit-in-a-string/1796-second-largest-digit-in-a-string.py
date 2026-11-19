class Solution:
    def secondHighest(self, s: str) -> int:
        max_=-1
        second_=-1
        for i in s:
            if i.isdigit():
                if int(i)>max_:
                    second_=max_
                    max_=int(i)
                elif int(i)<max_ and int(i)>second_:
                    second_=int(i)
        return second_
        
        
            
