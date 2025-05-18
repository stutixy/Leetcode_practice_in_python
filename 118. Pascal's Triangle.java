class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> ans = new ArrayList<List<Integer>>();
        List<Integer> first = new ArrayList<Integer>();
        first.add(1);
        ans.add(first);
        for(int i=1; i<numRows; i++){
            List<Integer> last = ans.get(i-1);
            List<Integer> newList = new ArrayList<Integer>();
            newList.add(1);
            for(int j=1; j<last.size(); j++){
              newList.add(last.get(j)+last.get(j-1));  
            }
            newList.add(1);
            ans.add(newList);
        }
        return ans;
    }
}