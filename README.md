![banner](https://github.com/EmikoHigashi/emikosh/blob/main/blob/banner.png)

🌀 迷路をつくろう！
Python で「自分だけの迷路」を作るプログラムです。

このリポジトリでは、
コンピュータに迷路をつくらせて、スタートとゴールを色で表示する  
という楽しい体験ができます。

🎮 これはなに？
コンピュータがランダムに道をほって、迷路をつくります

スタートは みどり

ゴールは あか

できた迷路は、絵として表示されます

「プログラムで世界ができあがる」感じがわかるよ。

🧠 どうして迷路をつくれるの？
このプログラムは、
「道をほる → 進む → 行き止まりなら戻る」  
という方法で迷路を作っています。

これは「深さ優先探索（DFS）」という考え方で、
ゲームづくりやロボットにも使われる大事なアルゴリズムです。

🛠 つかっているもの
Python

numpy

matplotlib

random

どれも子どもでも使える、やさしいライブラリです。

▶️ 実行するとどうなるの？
こんな感じの迷路ができます：

白いところ：通れる道

黒いところ：壁

みどり：スタート

あか：ゴール

毎回ちがう迷路ができるので、何度でも遊べます。

📦 ファイルの説明
generate_maze(width, height)  
→ 迷路をつくる関数

display_maze_with_start_goal(maze)  
→ スタートとゴールを色つきで表示する関数

width, height  
→ 迷路の大きさを決める数字
（大きくするとむずかしい迷路になる）

🌱 こんな子におすすめ
プログラミングをはじめたい

自分で世界をつくってみたい

ゲームづくりに興味がある

アルゴリズムを体験してみたい

🇺🇸 README (Kid-Friendly English Version)
🌀 Let’s Make a Maze!
This project lets you create your own maze using Python.

The computer digs paths, builds walls, and shows the maze as a picture.
The start is green, and the goal is red.

🎮 What does this program do?
The computer creates a maze randomly

The start point is green

The goal point is red

The maze is shown as an image

Every time you run it, you get a new maze

It feels like “building a world with code.”

🧠 How does the maze work?
The program uses a method called Depth-First Search (DFS):

Dig a path

Move forward

If you get stuck, go back

Keep digging until the maze is complete

This idea is used in games, robots, and many computer programs.

🛠 What libraries are used?
Python

numpy

matplotlib

random

These are simple and great for beginners.

▶️ What happens when you run it?
You will see:

White: paths

Black: walls

Green: start

Red: goal

Every maze is different!

📦 Files
generate_maze(width, height)  
→ Creates the maze

display_maze_with_start_goal(maze)  
→ Shows the maze with colors

width, height  
→ Change these numbers to make bigger or smaller mazes

🌱 Recommended for kids who…
Want to start programming

Want to build their own worlds

Like games and puzzles

Want to learn algorithms by doing
