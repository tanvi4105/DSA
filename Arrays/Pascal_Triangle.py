class PascalTriangle:
    def FindElement(r,c):
        n=r-1
        k=c-1
        res=1
        for i in range(k):
            res=res*(n-i)
            res=res//(i+1)
        return res
    
if __name__=="__main__":
    obj=PascalTriangle
    print(obj.FindElement(5,3)) 