class Solution {
    public boolean check(int[] nums) {
        int minIndex = 0;
        for (int i=1; i<nums.length; i++){
            if (nums[i] < nums[i-1]) {
                minIndex = i;
                break;
            }
        }
        
        int i = (minIndex+1) % nums.length;
        int prev = minIndex;
        while(i != minIndex){
            if(nums[prev] > nums[i])
                return false;
            prev = i;
            i = (i+1) % nums.length;
        }
        return true;
    }
}
