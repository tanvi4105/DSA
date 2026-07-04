#include<iostream>
#include<vector>
using namespace std;
class Solution {
public:
    void merge(vector<int>& A, int m, vector<int>& B, int n) {
        int idx=m+n-1, i=m-1, j=n-1;

        while(i>=0 && j>=0)
        {
            if(A[i]>=B[j])
            {
                A[idx]=A[i];
                idx--,i--;
                
            }
            else
            {
                A[idx]=B[j];
                idx--,j--;
            }
        }

        while(j>=0)
        {
            A[idx]=B[j];
            idx--,j--;
        }
        
    }
};
int main()
{
	Solution obj;
	vector<int> A={1,4,5,0,0,0}, B={2,3,7};
	int m=3, n=3;
	obj.merge(A,m,B,n);
	
	for(int val:A)
	{
		cout<<val<<" ";
	}
	
	return 0;
	
}
