class Solution {
    public int heightChecker(int[] heights) {
        int maxSize = 101;
        int[] count = new int[maxSize];
        for (int i=0; i<heights.length; i++){
            count[heights[i]] += 1;
        }
        int j = 0;
        int res = 0;
        for (int i=0; i<heights.length; i++){
            while(j<maxSize && count[j] == 0){
                j++;
            }
            if(j==maxSize){
                return res;
            }
            if(j != heights[i]){
                res += 1; 
            }
            count[j] -= 1;
        }
        return res;
    }
}