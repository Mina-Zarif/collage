from typing import List, Tuple

def convert_eight_path_to_four_path(eight_path: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    """Convert an 8-path to a 4-path.
    
    Args:
        eight_path: A list of tuples representing vertices.
        
    Returns:
        A list of tuples representing the 4-path.
    """
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    result = []
    current_vertex = eight_path[0]
    for next_vertex in eight_path[1:]:
        diagonal_directions = [(next_vertex[0] + p[0], next_vertex[1] + p[1]) for p in directions]
        straight_directions = [(current_vertex[0] + p[0], current_vertex[1] + p[1]) for p in directions]
        if next_vertex in straight_directions:
            result.append(next_vertex)
        else:
            for v in diagonal_directions:
                if v in straight_directions:
                    result.append(v)
                    break
        current_vertex = next_vertex
        result.append(current_vertex)
    return result

def draw_path(path: List[Tuple[int, int]]):
    """Draw the image showing the path."""
    max_x, max_y = max(coord[0] for coord in path), max(coord[1] for coord in path)
    for y in range(max_y + 1):
        for x in range(max_x + 1):
            print(1 if (x, y) in path else 0, end=" ")
        print()

if __name__ == '__main__':
    test_eight_path = [(0, 1), (1, 2), (2, 3), (3, 4)]
    draw_path(test_eight_path)
    print("\n-----------------\n")
    draw_path(convert_eight_path_to_four_path(test_eight_path))
