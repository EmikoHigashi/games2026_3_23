import matplotlib.pyplot as plt
import numpy as np
import random

def generate_maze(width, height):
    maze = np.ones((2 * height + 1, 2 * width + 1), dtype=int)

    def carve(x, y):
        dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        random.shuffle(dirs)
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < width and 0 <= ny < height and maze[2 * ny + 1][2 * nx + 1] == 1:
                maze[2 * y + 1 + dy][2 * x + 1 + dx] = 0
                maze[2 * ny + 1][2 * nx + 1] = 0
                carve(nx, ny)

    maze[1][1] = 0
    carve(0, 0)
    return maze

def display_maze_with_start_goal(maze):
    maze_display = maze.copy()
    start = (1, 1)
    goal = (maze.shape[0] - 2, maze.shape[1] - 2)

    # スタートとゴールを特別な値でマーク（2: スタート, 3: ゴール）
    maze_display[start] = 2
    maze_display[goal] = 3

    # カラーマップの定義
    from matplotlib.colors import ListedColormap
    cmap = ListedColormap(['white', 'black', 'green', 'red'])  # 0:通路, 1:壁, 2:スタート, 3:ゴール

    plt.figure(figsize=(10, 5))
    plt.imshow(maze_display, cmap=cmap)
    plt.axis('off')
    plt.title("Maze with Start (green) and Goal (red)")
    plt.show()

# 迷路のサイズ（幅×高さ）
width, height = 15, 10
maze = generate_maze(width, height)
display_maze_with_start_goal(maze)
