class Solution {
    public String destCity(List<List<String>> paths) {
        Map<String, String> path = new HashMap<>();
        for(int i=0; i<paths.size(); i++){
            path.put(paths.get(i).get(0), paths.get(i).get(1));
            if(!path.containsKey(paths.get(i).get(1)))
                path.put(paths.get(i).get(1), "");
        } 

        for(String key : path.keySet()){
            if(path.get(key).isEmpty()){
                return key;
            }
        }
        return "";
    }
}