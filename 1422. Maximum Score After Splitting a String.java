class Solution {
    public int maxScore(String s) {
        int[] zeroes = new int[s.length()];
        int[] ones = new int[s.length()];
        zeroes[0] = 0;
        ones[s.length()-1] = 0;

        for (int i=0; i<s.length(); i++){
            if( s.charAt(i) == '0') {
                zeroes[i] = i==0 ? 1:zeroes[i-1] + 1;
            } else {
                zeroes[i] = i==0 ? 0: zeroes[i-1];
            }
        }
        for (int i=s.length()-1; i>=0; i--){
            if( s.charAt(i) == '1') {
                ones[i] = i==s.length()-1 ? 1 : ones[i+1]+1;
            } else {
                ones[i] = i==s.length()-1 ? 0 : ones[i+1];
            }
        }
        int maxScore = 0;
        for (int i=1; i<s.length(); i++){
            maxScore = Math.max(maxScore, zeroes[i-1]+ones[i]);
        }
        return maxScore;
    }
}