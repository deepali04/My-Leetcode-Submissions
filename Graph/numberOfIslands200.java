class Solution {
    public int numIslands(char[][] grid) {
        //invalid conditions
        if(grid == null || grid.length == 0 || grid[0].length == 0)
            return 0;

        int count = 0;
        for(int i = 0; i < grid.length; i++){
            for(int j= 0; j < grid[0].length; j++){
                if(grid[i][j] == '1'){
                    count++ ;
                    dfs(grid, i, j);    
                }      
            }
        }
        return count;

    }

    private void dfs(char[][] grid, int i, int j){

        //invalid position or 0
        if( i < 0 || i>= grid.length || j < 0 || j >= grid[i].length || grid[i][j] != '1'){
            return;
        }

        //marking as visited
        grid[i][j] = 'X';

        //checking neighbours
        dfs(grid, i-1, j);
        dfs(grid, i+1, j);
        dfs(grid, i, j-1);
        dfs(grid, i, j+1);
    }
}