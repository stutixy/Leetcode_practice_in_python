class Solution {
    public List<String> stringMatching(String[] words) {
        Set<String> ans = new HashSet<String>();
        for(int i=0; i<words.length; i++){
            for(int j=0; j<words.length;j++){
                if (j==i){
                    continue;
                }
                if (words[i].contains(words[j])){
                    ans.add(words[j]);
                }
            }
        }
        return new ArrayList<String>(ans);
    }
}