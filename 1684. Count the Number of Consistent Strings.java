class Solution {
    public int countConsistentStrings(String allowed, String[] words) {
        Set<Character> allowedSet = new HashSet<>();
        for(int i=0;i<allowed.length(); i++){
            allowedSet.add(allowed.charAt(i));
        }
        int res = 0;
        for(int i=0; i<words.length; i++){
            String word = words[i];
            boolean isConsistent = true;
            for(int j=0; j<word.length(); j++){
                char c = word.charAt(j);
                if(!allowedSet.contains(c)){
                    isConsistent = false;
                    break;
                }
            }
            if(isConsistent){
                res += 1;
            }
        }
        return res;
    }
}