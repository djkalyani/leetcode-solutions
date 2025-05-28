class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int len = nums.size();
        int j;
        for(int i=0; i<len; i++){
            if(nums[i]==target)
                return i;
        }
        for(j=0; j<len; j++){
            if(nums[j]>target)     //index to insert
                return j;
        }
        return j;
    }
};
