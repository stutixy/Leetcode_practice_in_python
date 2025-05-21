class Solution {
    public String longestCommonPrefix(String[] strs) {
        String s = strs[0];
       
        for(int i = 1; i<strs.length; i++){
            for (int j = 0; j<s.length(); j++){
                if(j>=strs[i].length() || s.charAt(j) != strs[i].charAt(j)){
                    s = s.substring(0,j);
                    break;
                }
            }
        } 
        return s;
    }
}