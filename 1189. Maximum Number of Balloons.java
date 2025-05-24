class Solution {
    public int maxNumberOfBalloons(String text) {
        Map<Character, Integer> balloon = new HashMap<>();
        Map<Character, Integer> textMap = new HashMap<>();

        int minInstance = Integer.MAX_VALUE;
        String balloonString = "balloon";

        for(int i = 0; i<balloonString.length(); i++){
            char c = balloonString.charAt(i);
            if (!balloon.containsKey(c))
                balloon.put(c,0);
            balloon.put(c, balloon.get(c)+1);
            textMap.put(c,0);
            System.out.println(balloon.get(c));
        }
        for (int i=0; i<text.length(); i++){
             char c = text.charAt(i);
             if (textMap.containsKey(c))
                textMap.put(c, textMap.get(c)+1);
        }
        for(int i = 0; i<balloonString.length(); i++){
            char c = balloonString.charAt(i);
            minInstance = Math.min(minInstance, (int) (textMap.get(c)/balloon.get(c)));
        }
        return minInstance;
    }
}