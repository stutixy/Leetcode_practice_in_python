class Solution {
    public boolean makeEqual(String[] words) {
        int n = words.length;
        Map<Character, Integer> freq = new HashMap<>();
        for (String word : words){
            for(int i=0; i<word.length(); i++){
                char c = word.charAt(i);
                if(freq.get(c) == null){
                    freq.put(c, 0);
                }
                freq.put(c, freq.get(c)+1);
            }
        }
        for(Character key: freq.keySet()){
            if(freq.get(key) % n != 0)
                return false;
        }
        return true;
    }
}