#include<iostream>
#include<vector>
using namespace std;
class Solution
{
	public:
	int majority_ele(vector<int> & nums)
	{
		// Moore's voting algorithm
		int element=0;
		int cnt=0;
		for(int num:nums)
		{
			if(cnt==0)
			{
				element=num;
			}
			if(num==element)
			{
				cnt++;
			}
			else
			{
				cnt--;
			}
		}
		return element;
	}
};
int main()
{
	Solution obj;
	vector<int> nums={1,2,3,2,2,1};
	cout<<"Majority Element is "<<obj.majority_ele(nums);
	return 0;
}
