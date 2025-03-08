# checking git connectivity
# This code uses DFS to traverse the Matrix Graph
# def dfs(matrix, row, col, visited, result):
#     rows, cols = len(matrix), len(matrix[0])
#     directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # Down, Up, Right, Left

#     # Mark the current cell as visited and add it to the result
#     visited[row][col] = True
#     result.append(matrix[row][col])

#     # Explore the neighbors
#     for dx, dy in directions:
#         new_row, new_col = row + dx, col + dy
#         if 0 <= new_row < rows and 0 <= new_col < cols and not visited[new_row][new_col]:
#             dfs(matrix, new_row, new_col, visited, result)

# def dfs_traversal(matrix):
#     if not matrix or not matrix[0]:
#         return []

#     rows, cols = len(matrix), len(matrix[0])
#     visited = [[False for _ in range(cols)] for _ in range(rows)]
#     result = []

#     # Start DFS from the top-left corner (0, 0)
#     dfs(matrix, 0, 0, visited, result)
#     return result

# # Example usage:
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# print(dfs_traversal(matrix))
