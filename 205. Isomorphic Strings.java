class Solution {
    public boolean isIsomorphic(String s, String t) {
        if(s.length() != t.length()){
            return false;
        }
        Map<Character, Character> charMapS = new HashMap<>();
        Map<Character, Character> charMapT = new HashMap<>();

        for(int i=0; i<s.length(); i++){
            if(charMapS.containsKey(s.charAt(i))){
               if(charMapS.get(s.charAt(i)) != t.charAt(i)){
                    return false;
                } 
            } else if(charMapT.containsKey(t.charAt(i))){
               if(charMapT.get(t.charAt(i)) != s.charAt(i)){
                    return false;
                } 
            } 
            else {
                charMapS.put(s.charAt(i), t.charAt(i)); 
                charMapT.put(t.charAt(i), s.charAt(i)); 
            }
        }
        return true;
    }
}