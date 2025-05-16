/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    public boolean isBalanced(TreeNode root) {
        return helper(root).isBalanced;
    }

    public Result helper(TreeNode node){
            if(node == null) {
                return new Result(true, 0);
            }
            Result left = helper(node.left);
            if (!left.isBalanced){
                return new Result(false, 0);
            }
            Result right = helper(node.right);
            if (!right.isBalanced){
                return new Result(false, 0);
            }
            
            int diff =  Math.abs(left.height - right.height);
            if (diff > 1){
                return new Result(false, 0);
            } 
            return new Result(true, 1 + Math.max(left.height, right.height)); 
        }
}

class Result {
    boolean isBalanced = true;
    int height = 0;

    Result(boolean isBalanced, int height){
        this.isBalanced = isBalanced;
        this.height = height;
    }

}
