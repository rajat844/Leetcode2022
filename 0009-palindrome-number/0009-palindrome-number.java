class Solution {
    public boolean isPalindrome(int x) {
        if(x < 0){
            return false;
        }
        String s = String.valueOf(x);
        int i = 0;
        int j = s.length() - 1;
        
        while(i <= j){
            if (s.charAt(i) == s.charAt(j)){
                i += 1;
                j -= 1;
            }
            else return false;
        }
        return true;
    }
}