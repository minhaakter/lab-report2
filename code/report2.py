class MazeSolver:
    def __init__(self, grid, start, target):
        self.grid = grid
        self.start = start
        self.target = target
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def depth_limited_search(self, node, depth, path, visited):
        if node == self.target:
            return True, path
        if depth == 0:
            return False, []
        visited.add(node)
        for dx, dy in self.directions:
            new_x, new_y = node[0] + dx, node[1] + dy
            if (0 <= new_x < self.rows and 0 <= new_y < self.cols and
                    (new_x, new_y) not in visited and self.grid[new_x][new_y] == 0):
                found, result_path = self.depth_limited_search((new_x, new_y), depth - 1, path + [(new_x, new_y)], visited)
                if found:
                    return True, result_path
        visited.remove(node)
        return False, []

    def iddfs(self, max_depth):
        for depth in range(max_depth + 1):
            visited = set()
            found, path = self.depth_limited_search(self.start, depth, [self.start], visited)
            if found:
                return f"Path found at depth {depth} using IDDFS\nTraversal Order: {path}"
        return f"Path not found at max depth {max_depth} using IDDFS"

if __name__ == "__main__":
    rows, cols = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(rows)]
    sx, sy = map(int, input().split()[1:])
    tx, ty = map(int, input().split()[1:])
    solver = MazeSolver(grid, (sx, sy), (tx, ty))
    max_depth = max_depth = 6  
print(solver.iddfs(max_depth))
 
