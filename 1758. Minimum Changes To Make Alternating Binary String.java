class Solution {
    public int minOperations(String s) {
        if(s.length()<2){
            return 0;
        }
        char val = '0';
        int ops1 = 0; 
        for(int i=0; i<s.length(); i++){
            if(s.charAt(i) != val){
                ops1 += 1;
            }
            if(val == '0'){
                val = '1';
            } else {
                val = '0';
            }
        }
        val = '1';
        int ops2 = 0; 
        for(int i=0; i<s.length(); i++){
            if(s.charAt(i) != val){
                ops2 += 1;
            }
            if(val == '1'){
                val = '0';
            } else {
                val = '1';
            }
        }
        return Math.min(ops1, ops2);
    }
}