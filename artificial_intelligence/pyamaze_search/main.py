from bfs_algo import bfs_search
from dfs_algo import dfs_search
from astar_algo import astar_search
from pyamaze import maze, agent, COLOR

if __name__ == '__main__':
    maze_obj = maze(15, 25)
    maze_obj.CreateMaze(theme=COLOR.light, loopPercent=20, loadMaze="maze--2024-03-30--08-56-20.csv")

    agent_a = agent(maze_obj, filled=True, footprints=True, color=COLOR.blue)
    agent_b = agent(maze_obj, footprints=True, color=COLOR.red)

    agent_x = agent(maze_obj, filled=True, footprints=True, color=COLOR.black)
    agent_y = agent(maze_obj, footprints=True, color=COLOR.yellow)

    agent_i = agent(maze_obj, filled=True, footprints=True, color=COLOR.cyan)
    agent_j = agent(maze_obj, footprints=True, color=COLOR.green)

    paths_dfs = dfs_search(maze_obj)
    maze_obj.tracePath({agent_a: paths_dfs[0]}, kill=True, delay=60)
    maze_obj.tracePath({agent_b: paths_dfs[1]}, delay=50)

    paths_bfs = bfs_search(maze_obj)
    maze_obj.tracePath({agent_x: paths_bfs[0]}, kill=True, delay=10)
    maze_obj.tracePath({agent_y: paths_bfs[1]}, delay=50)

    paths_astar = astar_search(maze_obj)
    maze_obj.tracePath({agent_i: paths_astar[0]}, kill=True, delay=60)
    maze_obj.tracePath({agent_j: paths_astar[1]}, delay=50)

    maze_obj.run()
