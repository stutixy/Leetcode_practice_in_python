class Solution {
    public boolean isHappy(int n) {
        String s = String.valueOf(n);
        Set<String> seen = new HashSet<String> ();
        while (true) {
            seen.add(s);
            int sum = 0;
            for(int i=0; i<s.length(); i++){
                int value = Character.getNumericValue(s.charAt(i));
                sum += value*value;
            }
            s = String.valueOf(sum);
            if (s.equals("1")){
                return true;
            }
            if (seen.contains(s)){
                return false;
            }
        }
    }
}
