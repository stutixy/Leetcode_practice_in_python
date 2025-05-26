class Solution {
    public List<Integer> getRow(int rowIndex) {
       List<Integer> prev = new ArrayList<>();
       prev.add(1);
       List<Integer> next = new ArrayList<>();
       while(rowIndex > 0){
        next.add(1);
        for(int i=1; i<prev.size();i++){
            next.add(prev.get(i)+prev.get(i-1));
        }
        next.add(1);
        prev.clear();
        prev.addAll(next);
        next.clear();
        rowIndex--;
       }
       return prev;
    }
}
