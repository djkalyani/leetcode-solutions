class Solution {
public:
    bool isPalindrome(int x) {
        long int num = 0;
        int x1;
        int temp = x;
        while(x>0){
            x1 = x%10;
            x=x/10;
            if(x>0){
                num = (num+x1)*10; 
            }
            else
            num = num+x1;
            
        }
        if(temp == num){
            return true;
        }
        else
            return false;
    }
};
