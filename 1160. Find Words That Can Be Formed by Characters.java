class Solution {
    public int countCharacters(String[] words, String chars) {
        Map<Character, Integer> freqMap = new HashMap<>(); 
        for(int i=0; i<chars.length(); i++){
            char c = chars.charAt(i);
            if(!freqMap.containsKey(c)){
                freqMap.put(c, 0);
            }
            freqMap.put(c, freqMap.get(c)+1);
        }
        int sum = 0;
        for(int i=0; i<words.length; i++){
            Map<Character, Integer> temp = new HashMap<>();
            temp.putAll(freqMap);
            String word = words[i];
            
            boolean considerLength = true;
           
            for(int j=0; j<word.length(); j++){
                char c = word.charAt(j);
                if(!temp.containsKey(c) || temp.get(c)==0){
                    considerLength = false;
                    break;
                }
                temp.put(c, temp.get(c)-1);
            }

            if (considerLength) {
                sum += word.length();
            }
        }
        return sum;
    }
}