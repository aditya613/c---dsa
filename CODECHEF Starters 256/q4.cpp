#include <bits/stdc++.h>
using namespace std;

int main() {
	
    int t;
    cin>>t;
    while(t--){
        int N;
        cin>>N;
        vector<int> nums(N);

        int Cr = 1, Cb = 1, Sr, Sb;

        for(int i=0;i<N;i++){
            cin>>nums[i];
        }

        Sr = nums[0];
        Sb = nums[1];

        for(int i=2;i<N;i++){

            if(((Cr+1)*(Sb) + (Cb)*(Sr+nums[i]))> ((Cr)*(Sb+nums[i]) + (Cb+1)*(Sr))){
                Cr++;
                Sr+=nums[i];
            }else{
                Cb++;
                Sb+=nums[i];
            }
           

        }

         cout<<((Cr)*(Sb) + (Cb)*(Sr))<<endl;


    }
}
///above is wrong approach

