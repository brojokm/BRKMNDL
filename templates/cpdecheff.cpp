#include <iostream>
using namespace std;

int main(){
	int t;
	cin>>t;
	while(t--){
		long long n,m;
		cin>>n>>m;
		long long r;
		r=n%m;
		if(r%2==0) cout<<"EVEN"<<endl;
		else cout<<"ODD"<<endl;

	}
	return 0;
}