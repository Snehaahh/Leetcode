class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n=len(matrix)
        #reverse the matrix vertically
        for r in range(n//2):
                matrix[r],matrix[n-(r+1)]=matrix[n-(r+1)],matrix[r]
        #transpose
        for r in range(n):
            for c in range(r+1,n):
                matrix[r][c],matrix[c][r]=matrix[c][r],matrix[r][c]
                
                
