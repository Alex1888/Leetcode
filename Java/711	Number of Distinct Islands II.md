# [711	Number of Distinct Islands II](https://leetcode.com/problems/number-of-distinct-islands-ii/description/)

* java 对于每一个岛，利用每两个点之间的距离组成一个map，key是dist， val是有多少对点
* 这个map就是它的特征值了

```java
class Solution {
    int[][] dirs = new int[][] {{0,1}, {1,0}, {-1,0}, {0,-1}};
    public int numDistinctIslands2(int[][] grid) {
        // 每一个map代表了一个island 的类型，key是dist val是这个dist的个数
        Set<Map<Integer, Integer>> set = new HashSet();

        for(int i=0; i<grid.length; i++) {
            for(int j=0; j<grid[0].length; j++) {
                if(grid[i][j] == 1) {
                    List<int[]> list = new ArrayList();
                    findIslands(grid, i, j, list);
                    Map<Integer, Integer> type = distances(list);
                    set.add(type);
                }
            }
        }

        return set.size();
    }

    private void findIslands(int[][] grid, int r, int c, List<int[]> list) {
        list.add(new int[] {r, c});            
        grid[r][c] = 0;

        for(int[] dir: dirs) {
            int i = r + dir[0];
            int j = c + dir[1];

            if(i < 0 || i >= grid.length || j<0 || j>= grid[0].length || grid[i][j] == 0) {
                continue;
            }

            findIslands(grid, i, j, list);
        }
    }

    private Map<Integer, Integer> distances(List<int[]> points) {
        Map<Integer, Integer> map = new HashMap();

        for(int i=0; i<points.size(); i++) {
            for(int j=i+1; j<points.size(); j++) {
                int dis = (points.get(i)[0]-points.get(j)[0]) * (points.get(i)[0]-points.get(j)[0])
                + (points.get(i)[1]-points.get(j)[1])* (points.get(i)[1]-points.get(j)[1]);

                map.put(dis, map.getOrDefault(dis, 0) + 1);
            }
        }

        return map;
    }
}

```
