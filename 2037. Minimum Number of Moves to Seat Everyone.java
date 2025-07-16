class Solution {
    public int minMovesToSeat(int[] seats, int[] students) {
        Arrays.sort(seats);
        Arrays.sort(students);
        int ans = 0;
        for (int i = seats.length-1; i>=0; i--) {
            ans += Math.abs(students[i] - seats[i]);
        }
        return ans;
    }
}
