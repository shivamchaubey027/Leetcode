class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original_color = image[sr][sc]
        if original_color == color:
            return image 

        def dfs(r, c):
            
            if r < 0 or c < 0 or r >= len(image) or c >= len(image[0]):
                return
            if image[r][c] != original_color:
                return

           
            image[r][c] = color

            
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        dfs(sr, sc)
        return image


#We do is check the colours on all sides, if its same as the source then we change the colour of it and then move there and check if all directions there have same source then we change the colour there too, basically recursion , 
##The game is of DFS here, we can identify graph stuff with the adjacents thingg, in graoh we can go on all sides unlike linkedlist or Binarytree where we have to move in heirarchy
