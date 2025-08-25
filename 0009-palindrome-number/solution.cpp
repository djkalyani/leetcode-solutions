class Solution {
public:
    bool isPalindrome(int x) {
        if(x<0)
        return false;
        long int num = 0;
        int x1;
        int temp = x;
        while(x!=0){
            x1 = x%10;
            num = num*10 + x1;
            x=x/10;
        }
        
        if(temp == num){
            return true;
        }
        else
            return false;
    }
};
