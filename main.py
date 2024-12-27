import os
import time as t

# 调节机器人搜索深度（数值越大，机器人越智能，但运行速度越慢）
SEARCH_DEPTH = 2

# 定义棋盘大小和玩家
BOARD_SIZE = 10
PLAYER_HUMAN = 1
PLAYER_ROBOT = 2
WIN_CONDITION = 5  # 五子连珠
CLEAN = True  # 判定下棋后是否清屏


# 初始化棋盘
def init_board():
    return [[0 for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]


# 打印棋盘
def print_board(board):
    # 打印列号
    print("  ", end="")
    for i in range(BOARD_SIZE):
        print(f"{i:2}", end="")
    print()

    # 打印每一行
    for i in range(BOARD_SIZE):
        print(f"{i:2}", end=" ")  # 打印行号
        for j in range(BOARD_SIZE):
            if board[i][j] == PLAYER_HUMAN:
                print("●", end=" ")
            elif board[i][j] == PLAYER_ROBOT:
                print("○", end=" ")
            else:
                print("·", end=" ")
        print()  # 换行


# 检查胜利
def check_win(board, player):
    for x in range(BOARD_SIZE):
        for y in range(BOARD_SIZE):
            if (
                check_direction(board, x, y, player, (1, 0))
                or check_direction(board, x, y, player, (0, 1))
                or check_direction(board, x, y, player, (1, 1))
                or check_direction(board, x, y, player, (1, -1))
            ):
                return True
    return False


# 检查某方向是否满足五子连珠
def check_direction(board, x, y, player, direction):
    dx, dy = direction
    count = 0
    for _ in range(WIN_CONDITION):
        if 0 <= x < BOARD_SIZE and 0 <= y < BOARD_SIZE and board[x][y] == player:
            count += 1
        else:
            break
        x += dx
        y += dy
    return count == WIN_CONDITION


# 评估函数
def evaluate_board(board):
    def score_line(line):
        score = 0
        for length in range(1, WIN_CONDITION + 1):
            if line.count(PLAYER_ROBOT) == length and line.count(PLAYER_HUMAN) == 0:
                score += 10**length
            if line.count(PLAYER_HUMAN) == length and line.count(PLAYER_ROBOT) == 0:
                score -= 10**length
        return score

    score = 0
    for x in range(BOARD_SIZE):
        for y in range(BOARD_SIZE):
            # 获取每个方向的连线
            directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
            for dx, dy in directions:
                line = []
                for i in range(-4, 5):  # 获取9格范围
                    nx, ny = x + i * dx, y + i * dy
                    if 0 <= nx < BOARD_SIZE and 0 <= ny < BOARD_SIZE:
                        line.append(board[nx][ny])
                score += score_line(line)
    return score


# Minimax + Alpha-Beta 剪枝
def minimax(board, depth, alpha, beta, maximizing):
    if depth == 0 or check_win(board, PLAYER_HUMAN) or check_win(board, PLAYER_ROBOT):
        return evaluate_board(board), None

    best_move = None
    if maximizing:
        max_eval = -float("inf")
        for x in range(BOARD_SIZE):
            for y in range(BOARD_SIZE):
                if board[x][y] == 0:
                    board[x][y] = PLAYER_ROBOT
                    eval, _ = minimax(board, depth - 1, alpha, beta, False)
                    board[x][y] = 0
                    if eval > max_eval:
                        max_eval = eval
                        best_move = (x, y)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval, best_move
    else:
        min_eval = float("inf")
        for x in range(BOARD_SIZE):
            for y in range(BOARD_SIZE):
                if board[x][y] == 0:
                    board[x][y] = PLAYER_HUMAN
                    eval, _ = minimax(board, depth - 1, alpha, beta, True)
                    board[x][y] = 0
                    if eval < min_eval:
                        min_eval = eval
                        best_move = (x, y)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval, best_move


# 机器人下棋
def robot_move(board):
    print("机器人正在思考...")
    _, move = minimax(board, depth=SEARCH_DEPTH, alpha=-float("inf"), beta=float("inf"), maximizing=True)
    clear_console()  # 清空终端
    if move:
        board[move[0]][move[1]] = PLAYER_ROBOT
    return move


# 清空终端
def clear_console():
    if CLEAN:
        os.system("cls" if os.name == "nt" else "clear")


# 主游戏循环
def play_game():
    os.system("cls" if os.name == "nt" else "clear")
    board = init_board()
    print_board(board)
    while True:
        # 玩家下棋
        while True:
            try:
                x, y = map(int, input("请输入你的落子位置（格式：x y）：").split())
                if 0 <= x < BOARD_SIZE and 0 <= y < BOARD_SIZE and board[x][y] == 0:
                    board[x][y] = PLAYER_HUMAN
                    break
                else:
                    print("输入无效，请重新输入！")
            except ValueError:
                print("输入格式错误，请重新输入！")

        print_board(board)
        if check_win(board, PLAYER_HUMAN):
            print("恭喜你获胜了！")
            break

        # 机器人下棋
        move = robot_move(board)
        if move:
            print(f"机器人落子：x={move[0]} y={move[1]}")
        else:
            print("机器人无棋可下！")
            break
        print_board(board)
        if check_win(board, PLAYER_ROBOT):
            print("机器人获胜！")
            break


# 开始游戏
if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    print("五子棋机器人")
    print("——————————————————")
    print("made from 轩轩TAT@2024")
    print("目前搜索深度为", SEARCH_DEPTH)
    while True:
        if input("是否开始游戏？(y/n) :") == "y":
            play_game()
            print("本轮已结束,即将返回上级菜单")
        else:
            print("游戏结束")
            break
