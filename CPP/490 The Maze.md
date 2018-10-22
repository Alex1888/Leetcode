# [490. The Maze](https://leetcode.com/problems/the-maze/description/)
* DFS的思路,就是从start选一个方向一直走到不能走位置,然后再在这个点出发继续选一个方向走,直到走完或者碰到destination
* 关键在于要记录是否该点已经访问过的visited数组; 因为有可能start这个点就已经是尽头了,不能再走了,此时如果没有visited数组的话,不能判断这个newStart是否就是原来的start
* while循环一直走到尽头,需要的点是它的前一个点

```c++
class Solution {
public:
    vector<vector<int>> dirs = {{1,0}, {0, 1}, {-1, 0}, {0,-1}};
    vector<vector<bool>> visited;
    bool hasPath(vector<vector<int>>& maze, vector<int>& start, vector<int>& destination) {
        int n = maze.size();
        int m = maze[0].size();
        visited = vector<vector<bool>>(n , vector<bool>(m, false));
        return helper(maze, start, destination);
    }
    
private:
    bool helper(vector<vector<int>>& maze, vector<int>& start, vector<int>& destination) {
        if(start == destination)
            return true;
        visited[start[0]][start[1]] = true;
        int n = maze.size();
        int m = maze[0].size();   
        
        bool res = false;
        for(auto dir : dirs){
            int x = start[0] + dir[0];
            int y = start[1] + dir[1];
            while(x >= 0 && x < n && y >=0 && y < m && maze[x][y] == 0){
                x += dir[0];
                y += dir[1];
            }
            x -= dir[0];
            y -= dir[1];
            if(visited[x][y] == false){
                vector<int> newStart = vector<int>{x, y};
                if(helper(maze, newStart, destination))
                    return true;
            }
        }
        return false;
    }
};

```

* BFS的解法
* http://www.cnblogs.com/grandyang/p/6381458.html

```c++
class Solution {
public:
    bool hasPath(vector<vector<int>>& maze, vector<int>& start, vector<int>& destination) {
        int n = maze.size();
        int m = maze[0].size();
        vector<vector<int>> dirs = {{1,0}, {0, 1}, {-1, 0}, {0, -1}};
        vector<vector<bool>> visited(n, vector<bool>(m, false));
        queue<vector<int>> q;
        q.push(start);
        visited[start[0]][start[1]] = true;
               
        while(!q.empty()){
            auto t = q.front(); q.pop();
            if(t == destination) return true;
            for(auto dir : dirs){
                int x = t[0] + dir[0];
                int y = t[1] + dir[1];
                while(x >=0 && x < n && y >=0 && y < m && maze[x][y] == 0){
                    x += dir[0];
                    y += dir[1];
                }
                x -= dir[0];
                y -= dir[1];
                if(visited[x][y] == false){
                    visited[x][y] = true;
                    q.push({x, y});
                }            
            }
        }
        return false;
    }
};
```
