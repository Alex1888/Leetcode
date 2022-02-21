# [95. Unique Binary Search Trees II](https://leetcode.com/problems/unique-binary-search-trees-ii/description/)
* 参考 https://leetcode.com/problems/unique-binary-search-trees-ii/discuss/31494/A-simple-recursive-solution
* 思路就是如果从第i个开始,那g(1, i-1) 和g(i+1, n) 分别为左右子树.这就有了递归公式
* 值得注意的是跳出递归的条件

```java
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public List<TreeNode> generateTrees(int n) {
        if(n == 0) return new ArrayList<TreeNode>();
        return genTrees(1, n);
    }
    
    public List<TreeNode> genTrees(int start, int end){
        List<TreeNode> list = new ArrayList<TreeNode>();
        if(start > end){
            list.add(null);
            return list;
        }
        
        if(start == end){
            list.add(new TreeNode(start));
            return list;
        }
        
        for(int i= start; i<=end; i++){
            List<TreeNode>  lnodes = genTrees(start, i-1);
            List<TreeNode>  rnodes = genTrees(i+1, end);
            for(TreeNode lnode : lnodes){
                for(TreeNode rnode : rnodes){
                    TreeNode root = new TreeNode(i);
                    root.left = lnode;
                    root.right = rnode;
                    list.add(root);
                }
            }
        }
        
        return list;
    }
}
```
