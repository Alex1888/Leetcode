# [1091. Shortest Path in Binary Matrix](https://leetcode.com/problems/shortest-path-in-binary-matrix/)

* java 标准bfs

```java
class Solution {
    private int[][] dirs = 
        new int[][] {{1,0}, {0,1}, {-1,0}, {0,-1}, {1,1},  {-1,1},  {1,-1}, {-1,-1}};
    
    public int shortestPathBinaryMatrix(int[][] grid) {
        int n = grid.length;
        Queue<int[]> q = new LinkedList();
        
        if(grid[0][0] == 1 || grid[n-1][n-1] == 1)
            return -1;
        if(n == 1) return 1;
        
        q.add(new int[]{0,0});
        int res = 0;
        
        while(!q.isEmpty()){
            int size = q.size();
            for(int i=0; i<size; i++){
                int[] cur = q.poll();
                // 提早结束，不要在for里判断
                if(cur[0] == n-1 && cur[1] == n-1) 
                    return res+1;
                
                for(int[] dir : dirs){
                    int x = cur[0] + dir[0];
                    int y = cur[1] + dir[1];
                    if(x < 0 || x >=n || y < 0 || y >=n || grid[x][y] == 1)
                        continue;
                
                    q.add(new int[] {x, y});
                    
                    // 马上把x，y设为已访问，不然大case过不了；
                    // 之所以可以提早设置，就是因为能进队就表示这个节点之前肯定是0
                    grid[x][y] = 1; 
                }
                //grid[cur[0]][cur[1]] = 1; 这里就没有必要了；而且只有这句没有上面的xy设置，会超时
            }
            res++;
        }
        
        return -1;
    }
}

```
