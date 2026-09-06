class Solution:
    def reverse_word(self,s):
        word=[]
        s1=""
        for i in s:
            if i!=" ":
                s1+=i
            else:    
                word.append(s1)
                s1=""
                
        if s1:
            word.append(s1)  

        word.reverse()
        return" ".join(word)

obj=Solution()
print(obj.reverse_word("welcome to the jungle"))
