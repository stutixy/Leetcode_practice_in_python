class Solution {
    public int maxProductDifference(int[] nums) {
        
        int[] max1 = new int[2];
        int[] max2 = new int[2];
        int[] min1 = new int[2];
        int[] min2 = new int[2];
        max1[0] = Integer.MIN_VALUE;
        max1[1] = -1;
        max2[0] = Integer.MIN_VALUE;
        max2[1] = -1;
        for(int i=0; i<nums.length; i++){
            if(max1[0] <= nums[i]){
                max2[0] = max1[0];
                max2[1] = max1[1]; 
                max1[0] = nums[i];
                max1[1] = i;
            } else if(max2[0] <= nums[i]){ 
                max2[0] = nums[i];
                max2[1] = i;
            }
        }
        min1[0] = Integer.MAX_VALUE;
        min1[1] = -1;
        min2[0] = Integer.MAX_VALUE;
        min2[1] = -1;
        for(int i=0; i<nums.length; i++){
            if(min1[0] >= nums[i] && max1[1] != i && max2[1] != i ){
                min2[0] = min1[0];
                min2[1] = min1[1]; 
                min1[0] = nums[i];
                min1[1] = i;
            } else if(min2[0] >= nums[i] && max1[1] != i && max2[1] != i  ){
                min2[0] = nums[i];
                min2[1] = i;
            }
        }
        System.out.println(max1[0] + "" + max2[0] + "" + min1[0] + "" + min2[0]);
        return max1[0]*max2[0] - min1[0]*min2[0];
    }
}