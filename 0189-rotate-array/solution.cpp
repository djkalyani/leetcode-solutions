class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        int n = nums.size();
        if(n==0) return;
        int r = k%n;
        if(r==0) return;
        vector<int> temp(n);
        for(int i=0; i<n; i++){
            temp[(i+r)%n] = nums[i];
        }
        nums = temp;
    }
};
        /*int r=k;
        if (r==nums.size())
        return;
        else if(k>nums.size())
            r = k%nums.size();
        else
        r = k;

         for(int i=1; i<=r; i++){
                int temp = nums[nums.size()-1];
                for(int j=nums.size()-2;j>=0;j--){
                    nums[j+1] = nums[j];
                }
                nums[0] = temp;
            }
    }
};*/

/*
or(int i=1;i<=k;i++){
            int temp = nums[nums.size()-1];
            for(int j=nums.size()-2;j>=0;j--){
                nums[j+1] = nums[j];
            }
            nums[0] = temp;
         }

*/
