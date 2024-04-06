def convert_8path_to_4path(eight_path: list[tuple]) -> list[tuple]:
    """Convert an 8-path to a 4-path.
    
    Args:
        eight_path: A list of tuples representing vertices.
        
    Returns:
        A list of tuples representing the 4-path.
    """
    vh_dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    result = []
    curr = eight_path[0]
    for nxt in eight_path[1:]:
        d_dirs_vh = [(nxt[0] + p[0], nxt[1] + p[1]) for p in vh_dirs]
        s_dirs_vh = [(curr[0] + p[0], curr[1] + p[1]) for p in vh_dirs]
        if nxt in s_dirs_vh:
            result.append(nxt)
        else:
            for v in d_dirs_vh:
                if v in s_dirs_vh:
                    result.append(v)
                    break
        curr = nxt
        result.append(curr)
    return result

def draw_path(path: list[tuple]):
    """Draw the image showing the path."""
    max_x = max(coord[0] for coord in path)
    max_y = max(coord[1] for coord in path)
    for y in range(max_y + 1):
        for x in range(max_x + 1):
            if (x, y) in path:
                print(1, end=" ")
            else:
                print(0, end=" ")
        print()

if __name__ == '__main__':
    test_eight_path = [(0, 1), (1, 2), (2, 3), (3, 4)]
    draw_path(test_eight_path)
    print("===============")
    draw_path(convert_8path_to_4path(test_eight_path))
