# [1996	The Number of Weak Characters in the Game](https://leetcode.com/problems/the-number-of-weak-characters-in-the-game/)


```java
class Solution {
    public int numberOfWeakCharacters(int[][] properties) {
        // 如果[0]相同，[1]按递减排序，这是为了当从后往前遍历时，[0]相同则大的[1]晚出现，不会造成res++
        Arrays.sort(properties, (a, b) -> a[0] == b[0] ? b[1]-a[1] : a[0] - b[0]);

        int res = 0;
        int maxDefense = 0;

        //从后往前遍历，记录目前为止出现的maxDefense
        // 如果当前为止bimaxDefense 小，则得到一个答案，因为当前的attack必然bi之前的小，巧妙！
        for(int i=properties.length-1; i>=0; i--) {
            if(properties[i][1] < maxDefense) {
                res++;
            }

            maxDefense = Math.max(maxDefense, properties[i][1]);
        }

        return res;
    }
}


```
