class Solution:
    def rotate_matrix(self,arr):
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                arr[i][j],arr[j][i]=arr[j][i],arr[i][j]
            arr[i].reverse()
        return arr

arr=[[1,2,3],[4,5,6],[7,8,9]]
obj=Solution()
print(obj.rotate_matrix(arr))   
