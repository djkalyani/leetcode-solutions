class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int count=0;
        int size=nums.size();
        int i=0;
        for(int j=0;j<size;j++){
            if(nums[j]!=val){
                nums[i]=nums[j];
                i++;
            }
        }
        return i;
    }
};
