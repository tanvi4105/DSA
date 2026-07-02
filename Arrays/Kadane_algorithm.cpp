#include<iostream>
#include<vector>
#include<climits>
using namespace std;
class Solution
{
	public:
	int MaxSubArray(vector<int> & nums)
	{
		int currsum=0, maxsum=INT_MIN;
		for(int val: nums)
		{
			currsum+=val;
			maxsum=max(currsum,maxsum);
			if(currsum<0)
			{
				currsum=0;
			}
			
		}
		return maxsum;
	}
};
int main()
{
	Solution obj;
	
	vector<int> nums = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
    	int n = sizeof(nums) / sizeof(nums[0]);
	
	
	cout<<"Maximum Subarray Sum:"<<obj.MaxSubArray(nums)<<endl;
	
	return 0;
}
