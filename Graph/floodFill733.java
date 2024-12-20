class Solution {
    int prevColor,newColor;
    
    public int[][] floodFill(int[][] image, int sr, int sc, int color) {
        prevColor = image[sr][sc];
        this.newColor = color;
        if(prevColor == color) return image;
        dfs(image, sr, sc);
        return image;
    }

    private void dfs(int[][] image, int r, int c){
        if(r < 0 || r >= image.length || c < 0 || c >= image[0].length|| image[r][c] != prevColor){
            return;
        }

        image[r][c] = newColor;
        //adjacent check and pass to dfs
        dfs(image, r-1, c);
        dfs(image, r+1, c);
        dfs(image, r, c-1);
        dfs(image, r, c+1);
    }
}