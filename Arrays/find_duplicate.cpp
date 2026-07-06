#include<iostream>
#include<vector>
using namespace std;
class Solution 
{
public:
    int findDuplicate(vector<int>& nums) 
    {
        int slow=nums[0], fast=nums[0];

        do
        {
            slow=nums[slow];
            fast=nums[nums[fast]];
        }while(slow != fast);
        
        slow=nums[0];
        while(slow != fast)
        {
            slow=nums[slow];
            fast=nums[fast];
        }

        return slow;
    }
};
int main()
{
	Solution obj;
	vector<int> nums={1,2,3,2,5,6};
	
	cout<<"Duplicate Number is:"<<obj.findDuplicate(nums);
	return 0;
}
