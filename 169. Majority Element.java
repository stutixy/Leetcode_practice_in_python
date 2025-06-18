class Solution {
    public int majorityElement(int[] nums) {
        int freq = 1;
        int majority = nums[0];
        for(int i=1; i<nums.length; i++){
            if (nums[i] == majority){
                freq += 1;
            }else if (freq > 0){
                freq -= 1;
            } else{
                freq += 1;
                majority = nums[i];  
            }
        }
        return majority;
    }
}