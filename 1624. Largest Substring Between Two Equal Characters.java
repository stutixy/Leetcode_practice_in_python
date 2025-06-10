class Solution {
    public int maxLengthBetweenEqualCharacters(String s) {
        Map<Character, Integer> indexMap = new HashMap<>();
        int maxLen = -1;
        for (int i=0; i<s.length(); i++){
            char c = s.charAt(i);
            if(indexMap.containsKey(c)){
                maxLen = Math.max(maxLen, i-indexMap.get(c)-1);
            } else {
                indexMap.put(c, i);
            }
        }
        return maxLen;
    }
}