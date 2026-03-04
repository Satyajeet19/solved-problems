
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        candidate_positions = []
        valid_columns = set()
        rows, cols = len(mat), len(mat[0])
        
        for i in range(rows):
            ones_count = 0
            col_index = 0
            for j in range(cols):
                if mat[i][j] == 1:
                    ones_count += 1
                    col_index = j
            if ones_count == 1:
                candidate_positions.append((i, col_index))
        
        for j in range(cols):
            ones_count = 0
            for i in range(rows):
                if mat[i][j] == 1:
                    ones_count += 1
            if ones_count == 1:
                valid_columns.add(j)
    
        special_count = 0
        for row, col in candidate_positions:
            if col in valid_columns:
                special_count += 1
        return special_count