from collections import deque
from pyamaze import maze, agent, COLOR

def dfs_search(maze_obj):
    """Depth-first traversal"""
    start_point = (maze_obj.rows, maze_obj.cols)
    stack = [start_point]
    visited = [start_point]
    source_path = []
    goal_path = {}

    while stack:
        current_point = stack.pop()
        source_path.append(current_point)

        if current_point == (1, 1):
            break

        for direction in "ESNW":
            if maze_obj.maze_map[current_point][direction]:
                if direction == 'E':
                    child_point = (current_point[0], current_point[1] + 1)
                elif direction == 'W':
                    child_point = (current_point[0], current_point[1] - 1)
                elif direction == 'S':
                    child_point = (current_point[0] + 1, current_point[1])
                elif direction == 'N':
                    child_point = (current_point[0] - 1, current_point[1])

                if child_point in visited:
                    continue

                visited.append(child_point)
                stack.append(child_point)
                goal_path[child_point] = current_point

    real_path = {}
    current_cell = (1, 1)
    while current_cell != start_point:
        real_path[goal_path[current_cell]] = current_cell
        current_cell = goal_path[current_cell]

    return source_path, real_path

if __name__ == '__main__':
    maze_obj = maze()
    maze_obj.CreateMaze(theme=COLOR.light)
    agent_a = agent(maze_obj, filled=True, footprints=True, color=COLOR.blue)
    agent_b = agent(maze_obj, footprints=True, color=COLOR.red)

    paths = dfs_search(maze_obj)
    maze_obj.tracePath({agent_a: paths[0]}, kill=True, delay=100)
    maze_obj.tracePath({agent_b: paths[1]}, delay=50)

    maze_obj.run()
