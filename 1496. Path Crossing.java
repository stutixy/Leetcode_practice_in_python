class Solution {
    public boolean isPathCrossing(String path) {
        int[] current = new int[2];
        Set<String> seen = new HashSet<String>();
        seen.add("0:0");
        for(int i=0; i<path.length(); i++){
            char c = path.charAt(i);
            if (c == 'N'){
                current[1]+=1;
            } else if (c == 'S') {
                current[1]-=1;
            } else if (c == 'E') {
                current[0]+=1;
            } else {
                current[0]-=1;
            }
            String pos = String.valueOf(current[0]) + ":" + String.valueOf(current[1]);
            if(seen.contains(pos)){
                System.out.println(pos);
                return true;
            } else {
                seen.add(pos);
            }
        }
        return false;
    }
}

