class Solution {
    public String kthDistinct(String[] arr, int k) {
       Map<String, Integer> freqMap = new HashMap<>();
       for(int i=0; i<arr.length; i++){
            if (!freqMap.containsKey(arr[i])){
                freqMap.put(arr[i], 0);
            }
            freqMap.put(arr[i], freqMap.get(arr[i])+1);
       }
       for(int i=0; i<arr.length; i++){
            if(freqMap.get(arr[i]) == 1){
                k -= 1;
            }
            if(k == 0){
                return arr[i];
            }
       }
       return "";  
    }
}