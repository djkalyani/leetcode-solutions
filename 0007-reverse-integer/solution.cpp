class Solution {
public:
    int reverse(int x) {
       int dig;
        long long rev=0;
        while(x!=0){
            dig = x%10;
            rev = (rev*10)+dig;
            x=x/10;
        }
        if(rev < INT_MIN||rev > INT_MAX)
        {
            return 0;
        }
        else
        return rev;
    }
};
