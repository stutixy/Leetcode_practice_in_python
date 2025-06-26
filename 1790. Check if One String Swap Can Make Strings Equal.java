class Solution {
    public boolean areAlmostEqual(String s1, String s2) {
        char l1 = '\0';
        char l2 = '\0';
        int firstMismatch = -1;
        for (int i=0; i<s1.length(); i++){
            if (s1.charAt(i) != s2.charAt(i)){
                l1 = s1.charAt(i);
                l2 = s2.charAt(i);
                firstMismatch = i;
                break;
            }
        }
        if (firstMismatch == -1){
            return true;
        }
        int secondMismatch = -1;
        for (int i=firstMismatch + 1; i<s1.length(); i++){
            if (s1.charAt(i) == l2 && s2.charAt(i) == l1){
               secondMismatch = i;
               break;
            }
        }
        if (secondMismatch == -1){
            return false;
        }
        for (int i = 0; i<s1.length(); i++) {
            if (i == secondMismatch || i == firstMismatch){
                continue;
            }
            if (s1.charAt(i) != s2.charAt(i)){
                return false;
            }
        }
        return true;
    }
}
