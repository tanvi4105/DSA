#include<iostream>
using namespace std;
class Solution 
{
public:
    double Pow(double x, int n) 
    {
	    if(n==0) return 1.0;
	    if(x==0) return 0.0;
	    if(x==1) return 1.0;
	    long long N = n;

	    if(n<0)
	    {
		x=1/x;
		N=-N;
	    }

	    double ans=1;
	    while(N>0)
	    {
		if(N%2 == 1)
		{
		    ans*=x;
		    N=N-1;
		}
		else
		{
		    x=x*x;
		    N=N/2;
		}
	    }
	    return ans;
    }
};
int main()
{
	Solution obj;
	double x=2.0;
	int n=15;
	
	double result= obj.Pow(x,n);
	
	cout<<"Power of "<<x<<" is "<<result;
	return 0;
}
