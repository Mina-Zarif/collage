from turtle import color
from pyamaze import maze, agent, COLOR
from util import PriorityQueue

def manhattan_distance(point):
    return (point[0] - 1) + (point[1] - 1)

def astar_search(maze_obj):
    start_point = (maze_obj.rows, maze_obj.cols)
    priority_queue = PriorityQueue()
    visited = [start_point]
    source_path = []
    goal_path = {}
    priority_queue.push(start_point, manhattan_distance(start_point))

    while not priority_queue.isEmpty():
        current_point = priority_queue.pop()
        source_path.append(current_point)

        if current_point == (1, 1):
            break

        for direction in "ESNW":
            if maze_obj.maze_map[current_point][direction] == True:
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
                priority_queue.push(child_point, manhattan_distance(child_point))
                goal_path[child_point] = current_point

    real_path = {}
    current_cell = (1, 1)
    while current_cell != start_point:
        real_path[goal_path[current_cell]] = current_cell
        current_cell = goal_path[current_cell]

    return source_path, real_path

if __name__ == '__main__':
    maze_obj = maze(15, 15)
    maze_obj.CreateMaze(theme=COLOR.light, loopPercent=10,)
    agent_a = agent(maze_obj, filled=True, footprints=True, color=COLOR.yellow)
    agent_b = agent(maze_obj, footprints=True, color=COLOR.red)

    paths = astar_search(maze_obj)
    maze_obj.tracePath({agent_a: paths[0]}, kill=True, delay=60)
    maze_obj.tracePath({agent_b: paths[1]}, delay=50)

    maze_obj.run()
