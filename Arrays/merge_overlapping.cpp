#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
class Solution
{
	public:
	vector<vector<int>> mergeOverlapping(vector<vector<int>> & arr)
	{
		int n=arr.size();
		sort(arr.begin(),arr.end());
		vector<vector<int>> ans;
		for(int i=0;i<n;i++)
		{
			if(ans.empty() || arr[i][0]>ans.back()[1])
			{
				ans.push_back(arr[i]);
			}
			else
			{
				ans.back()[1]=max(ans.back()[1],arr[i][1]);
			}
		}
		return ans;
		
	}
	
};
int main()
{
	Solution obj;
	vector<vector<int>> arr={{1,2},{2,4},{2,6},{8,10},{8,9},{9,11},{15,18},{16,17}};
	vector<vector<int>> ans=obj.mergeOverlapping(arr);
	
	cout<<"merge overlapping:";
	
	for (int i = 0; i < ans.size(); i++)
	{
    	cout << "[" << ans[i][0] << ", " << ans[i][1] << "] ";
	}
	return 0;
}
