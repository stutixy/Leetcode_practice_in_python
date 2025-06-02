class Solution {
    public int numIdenticalPairs(int[] nums) {
        Map<Integer, Integer> freq = new HashMap<>();
        for(int i=0; i<nums.length; i++){
            if(!freq.containsKey(nums[i])){
                freq.put(nums[i], 0);
            }
            freq.put(nums[i], freq.get(nums[i])+1);
        }
        int res = 0;
        for(int key: freq.keySet()){
            res += numPairs(freq.get(key));
        }
        return res;
    }
    public int numPairs(int num){
        return (num * (num - 1))/2;
    }
}
